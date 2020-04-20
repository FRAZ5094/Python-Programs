
from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

class MultiWindowApp(App):
    def build(self):
        return kv

kv=Builder.load_file("MultiWindow.kv")

if __name__=="__main__":
    MultiWindowApp().run()
    import os 
    os._exit(00)
    