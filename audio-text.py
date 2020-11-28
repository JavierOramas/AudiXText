import speech_recognition as sr
from pathlib import Path
import typer

def audio_to_text(file:typer.Argument(default='input.wav')):
    listener = sr.Recognizer()
    with file as source:
        audio = listener.record(source)
    
    return listener.recognize_google(audio)
