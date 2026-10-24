import time
from pathlib import Path
import fermion

MODEL_NAME = "phonon-2"
AUDIO_FILENAME = ""
AUDIO_EXTENSIONS = {".wav", ".flac", ".mp3", ".m4a"}

def find_audio_file():
    folder = Path(__file__).resolve().parent
    if AUDIO_FILENAME:
        path = folder / AUDIO_FILENAME
        if not path.is_file():
            raise FileNotFoundError(f"Audio file not found: {path}")
        return path
    candidates = sorted(p for p in folder.iterdir() if p.suffix.lower() in AUDIO_EXTENSIONS)
    if not candidates:
        raise FileNotFoundError(f"No audio file found in {folder}")
    return candidates[0]

def load_model():
    start = time.perf_counter()
    speech = fermion.load_speech(MODEL_NAME)
    print(f"Model loaded in {time.perf_counter() - start:.1f} s")
    return speech

def transcribe(speech, path):
    start = time.perf_counter()
    text, _, _ = speech.transcribe(str(path))
    print(f"Transcribed in {time.perf_counter() - start:.1f} s")
    return text

def main():
    path = find_audio_file()
    print(f"Audio file: {path.name}")
    speech = load_model()
    text = transcribe(speech, path)
    print()
    print(text)

if __name__ == "__main__":
    main()
