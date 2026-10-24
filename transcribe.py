import time
from pathlib import Path
import fermion

MODEL_NAME = "phonon-2"

def find_audio_file():
    folder = Path(__file__).resolve().parent
    while True:
        raw = input("Audio file path: ").strip().strip("'\"")
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

def main():
    path = find_audio_file()
    print(f"Audio file: {path.name}")
    speech = load_model()
    text = transcribe(speech, path)
    print()
    print(text)

if __name__ == "__main__":
    main()
