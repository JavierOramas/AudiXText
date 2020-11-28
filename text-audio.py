from gtts import gTTS
import typer

def text_to_audio(text = typer.Argument(), language =typer.Argument(default='es')):
     
    output = gTTS(text,lang=language)
    output.save('output.mp3')

    return True