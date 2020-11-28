# AudiXText Speech Interface

Tool for converting audio to text and tecxt to audio

## Installation 

`pip install -r requirements.txt`

## Execution

### Audio to Text

`python script.py Audio {path_to_audio} {lang} --noise-span {duration, default 1s} --show-alt {Bool, default False}`

### Text to Audio

`python script.py Text {path_to_text} {lang}`