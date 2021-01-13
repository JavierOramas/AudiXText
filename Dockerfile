FROM Ubuntu

RUN 'sudo apt-get update'
RUN 'sudo apt-get upgrade'
RUN 'sudo apt-get install python3'

# RUN 'wget ' getpip

RUN 'pip install -r requirements.txt'



