# AudiXText Speech Interface
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![GitHub contributors](https://img.shields.io/github/contributors/JavierOramas/AudiXText.svg)](https://GitHub.com/JavierOramas/AudiXText/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/JavierOramas/AudiXText.svg)](https://GitHub.com/JavierOramas/AudiXText/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/JavierOramas/AudiXText.svg)](https://GitHub.comJavierOramas/AudiXText/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/JavierOramas/AudiXText.svg)](https://GitHub.com/JavierOramas/AudiXText/pull/)
[![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/JavierOramas/AudiXText.svg)](https://GitHub.com/JavierOramas/AudiXText/pull/)

Tool for converting audio to text and tecxt to audio

## Installation 

`pip install -r requirements.txt`

## Execution

### Audio to Text

`python script.py Audio {path_to_audio} {lang} --noise-span {duration, default 1s} --show-alt {Bool, default False}`

### Text to Audio

`python script.py Text {path_to_text} {lang}`
