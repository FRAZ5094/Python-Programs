import tkinter as tk

root = tk.Tk()

e=tk.Entry(root,width=50,bg="White",fg="Blue",borderwidth=2)
e.pack()
e.insert(0,"Enter your name:") # intert changes the text in the entry by default

def myClick():
    myLabel=tk.Label(root,text="Hello " +e.get()) # e.get() gets text from the entry e
    myLabel.pack()

myButton=tk.Button(root,text="Enter your name",state="normal",padx=10,pady=10,fg="Blue",bg="Red",command=myClick)
myButton.pack()

root.mainloop()