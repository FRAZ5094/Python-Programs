import tkinter as tk

root = tk.Tk()

def button_click(number):
    myLabel=tk.Label(root,text=number)
    myLabel.pack()

myButton=tk.Button(root,text="Click",command=lambda: button_click("bitch"))
myButton.pack()
root.mainloop()