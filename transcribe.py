import time
from pathlib import Path
import fermion

MODEL_NAME = "phonon-2"
AUDIO_EXTENSIONS = {".wav", ".flac", ".mp3", ".m4a"}

def first_audio_file(folder):
    candidates = sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in AUDIO_EXTENSIONS)
    return candidates[0] if candidates else None

def find_audio_file():
    folder = Path(__file__).resolve().parent
    while True:
        raw = input("Audio file path (first in folder): ").strip().strip("'\"")
        if not raw:
            path = first_audio_file(folder)
            if path:
                return path
            print(f"No audio file found in {folder}")
            continue
        path = folder / Path(raw).expanduser()
        if path.is_file():
            return path
        print(f"Not a file: {path}")

def load_model():
    start = time.perf_counter()
    speech = fermion.load_speech(MODEL_NAME)
    if False: print(f"Model loaded in {time.perf_counter() - start:.1f} s")
    return speech

def transcribe(speech, path):
    start = time.perf_counter()
    text, _, _ = speech.transcribe(str(path))
    print(f"Transcribed in {time.perf_counter() - start:.1f} s")
    return text

def save_text(path, text):
    output_path = path.with_suffix(".txt")
    output_path.write_text(text, encoding="utf-8")
    return output_path

def main():
    path = find_audio_file()
    print(f"Audio file: {path.name}")
    speech = load_model()
    text = transcribe(speech, path)
    output_path = save_text(path, text)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    main()
