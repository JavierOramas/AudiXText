from typer import Typer, Argument,Option
from audio_text import audio_to_text
from text_audio import text_to_audio

app = Typer()

@app.command(help='Convert audio to text')
def Audio(file=Argument(default='input.mp3'), lang=Argument(default='es-ES'), noise_span = Option(default=1), show_alt = Option(default=False)):
    return audio_to_text(file=file, language=lang, noise_span=noise_span, show_alt=show_alt)

@app.command(help='Convert text to Audio')
def Text(text = Argument(default=''), lang = Argument(default='es')):
    return text_to_audio(text,language=lang)

if __name__ == '__main__':
    app()