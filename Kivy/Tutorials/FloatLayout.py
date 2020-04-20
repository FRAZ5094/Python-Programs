
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class FloatApp(App):
    def build(self):
        return FloatLayout()

if __name__=="__main__":
    
    FloatApp().run()
    import os 
    os._exit(00)