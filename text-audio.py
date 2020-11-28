import os
from gtts import gTTS


def text_to_audio(text = typer.Argument(), language =typer.Argument(default='es')):
     
    output = gTTS(text,lang=language)
    output.save('output.mp3')

    return True