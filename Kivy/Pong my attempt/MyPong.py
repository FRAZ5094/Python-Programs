from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

class PongGame(Widget):
    pass

class MyPongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    MyPongApp().run()
    import os 
    os._exit(00)