from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivymd.theming import ThemeManager

class MobileApp(App):
    theme_cls=ThemeManager()

MobileApp().run()