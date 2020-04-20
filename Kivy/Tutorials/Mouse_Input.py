from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.graphics import Ellipse

from kivy.core.window import Window

global d
d=5

class Touch(Widget):
    def __init__(self,**kwargs):
        super(Touch,self).__init__(**kwargs)
        with self.canvas:
            self.ellipse=Ellipse(pos=(-d,-d),size=(d,d))
            #self.line=Line(points=(0,0))

    def on_touch_down(self,touch):
        with self.canvas:
            self.line=Line(points=(touch.x,touch.y))
            #self.line.points=(touch.x,touch.y)
        self.ellipse.pos=(touch.x-d/2,touch.y-d/2)

    def on_touch_move(self,touch):
        self.line.points+=(touch.x,touch.y)
        self.ellipse.pos=(touch.x-d/2,touch.y-d/2)
     
    def on_touch_up(self,touch):
        pass


class InputApp(App):
    def build(self):    
        return Touch()

if __name__=="__main__":
    InputApp().run()
    import os 
    os._exit(00)