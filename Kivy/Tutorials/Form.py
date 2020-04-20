from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):

    def __init__(self,**kwargs): #**kwargs means dont know how many params function will get
        super(MyGrid,self).__init__(**kwargs)
        
        self.cols=1

        self.inside=GridLayout()
        self.inside.cols=2

        self.inside.add_widget(Label(text="First name: "))
        self.name= TextInput(multiline=False) #gets text from Input box
        self.inside.add_widget(self.name) #adds Input box to widgets

        self.inside.add_widget(Label(text="Last name: "))
        self.lastname= TextInput(multiline=False) 
        self.inside.add_widget(self.lastname) 

        self.inside.add_widget(Label(text="Email: "))
        self.email= TextInput(multiline=False) 
        self.inside.add_widget(self.email) 

        self.add_widget(self.inside)

        self.submit=Button(text="submit",font_size=40)
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.pressed)

    def pressed(self,instance):
        name=self.name.text
        last=self.lastname.text
        email=self.email.text
        print("Name: {}\nLast Name: {}\nEmail: {}".format(name,last,email))
        self.name.text=""
        self.lastname.text=""
        self.email.text=""
    

class FormApp(App):
    #dont need to __init__ because its already done when we call the app
    def build(self):
        return MyGrid() #draws all widgets from MyGrid
    

if __name__=="__main__":
    FormApp().run()
    import os 
    os._exit(00)