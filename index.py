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
            print(self.request.files)
            lang = self.request.files['lang'] 
        except:
            print('here')
            return None
        
        try:
            audio = self.request.files['audio']
        except:
            try:
                text = self.request.files['text']
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