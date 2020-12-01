import tornado.web
import tornado.ioloop
import json
from audio_text import audio_to_text
from text_audio import text_to_audio
import os

class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
        
    def post(self):
        lang = audio = text = None
        try:
            lang = str(self.request.arguments['lang'][0])[2:-1]
            # lang = str([x.decode('utf-8') for x in self.request.arguments['lang']])[2:-2]
        except:
            lang = self.request.arguments['lang'].decode('utf-8')
            return None
        
        try:
            audio = self.request.arguments['audio']
        except:
            try:
                text = str([x.decode('utf-8') for x in self.request.arguments['text']])[2:-2]
            except:
                return 'Invalid Data' 
        
        if audio is not None:
            for f in audio:
                fh = open('audio/input.wav', 'wb')
                fh.write(f.body)
                fh.close()
                
            resp = audio_to_text('audio/input.wav', language=lang)
            
            #saving text as txt temporary
            with open('text/output.txt') as file:
                file.write(resp)
                
            #start dowload of the file    
            
            os.remove('text/output.txt')
            os.remove('audio/input.mp3')
            
        
        if text is not None:
            text_to_audio(text,language=lang)
            
            # start download the file on the client
            
            os.remove('audio/output.mp3')
            

if __name__ == '__main__':
        
    conf = json.load(open('settings/config.json'))
    
    app = tornado.web.Application([
      ("/", uploadHandler),
      ("/audio", uploadHandler),  
      ("/text", uploadHandler)  
    ])
    
    app.listen(conf[port]) #to be changed
    print(f'listening on port {conf[port]}')

    tornado.ioloop.IOLoop.instance().start()
    