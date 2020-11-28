from gtts import gTTS

def text_to_audio(text, language ='es'):
     
    output = gTTS(text,lang=language)
    output.save('output.mp3')

    return True