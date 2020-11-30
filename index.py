import tornado.web
import tornado.ioloop
import json
import pandas as pd
from audio_text import audio_to_text
from text_audio import text_to_audio

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
                fh = open('audio/input.mp3', 'wb')
                fh.write(f.body)
                fh.close()
            # print('audio')
            print(audio_to_text('audio/input.mp3', language=lang))
        
        if text is not None:
            print(text)
            print(text_to_audio(text,language=lang))

if __name__ == '__main__':
        
    # conf = pd.read_json('config.json').to_dict(orient=str)    
    # print(conf.keys)
    
    app = tornado.web.Application([
      ("/", uploadHandler),
      ("/audio", uploadHandler),  
      ("/text", uploadHandler)  
    ])
    
    app.listen(8080) #to be changed
    print(f'listening on port 8080')
    
    tornado.ioloop.IOLoop.instance().start()