from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

#scale=0.25
#Config.set('graphics', 'width', str(int(1242*scale)))
#Config.set('graphics', 'height', str(int(2688*scale)))

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget): #pass in Widget if working with .kv??
    name=ObjectProperty(None)
    email=ObjectProperty(None)
    def btn(self): #dont need to pass instance because calling root.btn
        print("Name: {}\nEmail: {}".format(self.name.text,self.email.text))
        self.name.text=""
        self.email.text=""
        
class KvAppTestApp(App): #name .kv file same as MyApp but without out the "App" (if ends in app), all lower case
    def build(self):
        return MyGrid()


if __name__=="__main__":
    KvAppTestApp().run()
    import os 
    os._exit(00)