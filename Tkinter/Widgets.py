import tkinter as tk 

wind=tk.Tk()

wind.title("Widgets")

Frame=tk.Frame(wind)
Frame.pack()

tk.Label(Frame,text="This is our first Label").pack()
tk.Button(Frame,text="Hi im a button").pack()

#as variable
label2=tk.Label(Frame,text="Label 2")
label2.pack()


wind.mainloop()