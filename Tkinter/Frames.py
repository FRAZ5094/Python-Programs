import tkinter as tk
from PIL import ImageTk,Image

root=tk.Tk()
root.title("Frames")
icon=Image.open("Images/Calculator.ico")
root.iconphoto(False, ImageTk.PhotoImage(icon))


root.mainloop()