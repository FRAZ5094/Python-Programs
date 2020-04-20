import tkinter as tk

root = tk.Tk()

def myClick():
    myLabel=tk.Label(root,text="You clicked the Button")
    myLabel.pack()

myButton=tk.Button(root,text="Click me",state="normal",padx=10,pady=10,fg="Blue",bg="Red",command=myClick)
myButton.pack()

root.mainloop()