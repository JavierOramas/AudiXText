import speech_recognition as sr
from pathlib import Path

#this function recieves the file path, the language, the noise span for adjusting the noise reduction algorithm and the show_alt bool to toggle show all alternatives on transcription
def audio_to_text(file='input.wav', language='es-ES',noise_span=1, show_alt=False):
    #create the listener
    listener = sr.Recognizer()
    
    #load the file
    with file as source:
        #adjust it for the noise reduction
        listener.adjust_for_ambient_noise(source, duration=noise_span)
        #record it
        audio = listener.record(source)
    
    #get the trnascription made by google (other options can be used but this is the most popular)
    try:
        response = listener.recognize_google(audio, show_all=show_alt, language=language)
    except:
        response = 'Audio could not be transcrypted'
    
    return response
