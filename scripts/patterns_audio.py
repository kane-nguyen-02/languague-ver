#!/usr/bin/env python3
"""Generate one MP3 per language from <lang>/patterns.md (offline TTS).

Each sentence: target sentence -> pause -> Vietnamese meaning -> pause ->
target sentence again -> long pause (time to repeat aloud / shadowing).

Requirements: ffmpeg, `pip install sherpa-onnx pyopenjtalk-plus numpy`, and
sherpa-onnx VITS models extracted into MODELS_DIR (default ./models):
  https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/<name>.tar.bz2
  vits-piper-vi_VN-vais1000-medium, vits-piper-en_US-lessac-medium,
  vits-piper-zh_CN-huayan-medium, vits-mimic3-ko_KO-kss_low
Japanese uses pyopenjtalk (bundled voice).

Usage: python3 scripts/patterns_audio.py [MODELS_DIR] [en ja ko zh]
"""
import re
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SR = 24000
MODELS = {
    "vi": "vits-piper-vi_VN-vais1000-medium/vi_VN-vais1000-medium.onnx",
    "en": "vits-piper-en_US-lessac-medium/en_US-lessac-medium.onnx",
    "zh": "vits-piper-zh_CN-huayan-medium/zh_CN-huayan-medium.onnx",
    "ko": "vits-mimic3-ko_KO-kss_low/ko_KO-kss_low.onnx",
}
SPEED = {"vi": 1.0, "en": 0.9, "zh": 0.85, "ko": 0.85}
VI_ABBR = {
    "VN": "Việt Nam", "SV": "sinh viên", "GV": "giáo viên", "WC": "nhà vệ sinh",
    "TQ": "tiếng Trung", "BK": "Bắc Kinh", "bao tiền": "bao nhiêu tiền",
}
LATIN = re.compile(r"[A-Za-zÀ-ɏ]")


def parse(lang):
    """Return [(target_text, vietnamese_meaning_or_None)] from the 30-row table."""
    rows = []
    for line in (ROOT / lang / "patterns.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not cells[0].isdigit():
            continue
        pattern, example = cells[1], cells[2]
        meaning = cells[3] if len(cells) > 3 else None
        if lang == "en":
            text = example
        else:
            text = example
            if lang in ("ja", "zh"):  # drop romaji / pinyin after the native text
                m = LATIN.search(text)
                if m:
                    text = text[: m.start()]
        text = re.sub(r"([!?.])\s*/\s*", r"\1 ", text)
        text = text.replace(" / ", ", ").replace("/", ", ").strip()
        if meaning:
            meaning = meaning.replace(" / ", ", ")
            for k, v in VI_ABBR.items():
                meaning = re.sub(rf"\b{k}\b", v, meaning)
        rows.append((text, meaning))
    return rows


_tts_cache = {}


def sherpa_tts(lang, models_dir):
    if lang not in _tts_cache:
        import sherpa_onnx

        model = Path(models_dir) / MODELS[lang]
        cfg = sherpa_onnx.OfflineTtsConfig(
            model=sherpa_onnx.OfflineTtsModelConfig(
                vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                    model=str(model),
                    tokens=str(model.parent / "tokens.txt"),
                    data_dir=str(model.parent / "espeak-ng-data"),
                ),
                num_threads=4,
            )
        )
        _tts_cache[lang] = sherpa_onnx.OfflineTts(cfg)
    return _tts_cache[lang]


def resample(x, sr):
    if sr == SR:
        return x
    n = int(len(x) * SR / sr)
    return np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x)


def speak(lang, text, models_dir):
    if lang == "ja":
        import pyopenjtalk

        x, sr = pyopenjtalk.tts(text, speed=0.9)
        x = x / 32768.0
    else:
        audio = sherpa_tts(lang, models_dir).generate(text, sid=0, speed=SPEED[lang])
        x, sr = np.array(audio.samples), audio.sample_rate
    x = resample(np.asarray(x, dtype=np.float64), sr)
    peak = np.max(np.abs(x)) or 1.0
    return x / peak * 0.85


def silence(sec):
    return np.zeros(int(SR * sec))


def build(lang, models_dir):
    parts = []
    for i, (text, meaning) in enumerate(parse(lang), 1):
        print(f"[{lang}] {i:2d} {text} | {meaning}")
        target = speak(lang, text, models_dir)
        parts += [speak("vi", f"Câu {i}.", models_dir), silence(0.5), target, silence(1.2)]
        if meaning:
            parts += [speak("vi", meaning, models_dir), silence(1.0)]
        dur = len(target) / SR
        parts += [target, silence(max(2.5, dur * 1.5 + 1.0))]
    audio = (np.concatenate(parts) * 32767).astype(np.int16)
    out = ROOT / lang / "patterns.mp3"
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        with wave.open(tmp.name, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(SR)
            w.writeframes(audio.tobytes())
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", tmp.name, "-codec:a",
             "libmp3lame", "-b:a", "64k", "-metadata", f"title={lang.upper()} patterns", str(out)],
            check=True,
        )
    print(f"-> {out} ({len(audio) / SR / 60:.1f} min)")


if __name__ == "__main__":
    models_dir = sys.argv[1] if len(sys.argv) > 1 else "models"
    for lang in sys.argv[2:] or ["en", "ja", "ko", "zh"]:
        build(lang, models_dir)
