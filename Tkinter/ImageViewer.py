import tkinter as tk
from PIL import ImageTk,Image

scale=1

root=tk.Tk()
root.title("Rory Photos")
root.resizable(False,False)
icon=Image.open("Images/DogTrans.png")
root.iconphoto(False, ImageTk.PhotoImage(icon))

my_img1=Image.open("Images/Rory.png")
my_img1=ImageTk.PhotoImage(my_img1.resize((int(my_img1.size[0]*scale), int(my_img1.size[1]*scale)), Image.ANTIALIAS))

my_img2=Image.open("Images/Rory2.png")
my_img2=ImageTk.PhotoImage(my_img2.resize((int(my_img2.size[0]*scale), int(my_img2.size[1]*scale)), Image.ANTIALIAS))

my_img3=Image.open("Images/Rory3.png")
my_img3=ImageTk.PhotoImage(my_img3.resize((int(my_img3.size[0]*scale), int(my_img3.size[1]*scale)), Image.ANTIALIAS))

my_img4=Image.open("Images/Rory4.png")
my_img4=ImageTk.PhotoImage(my_img4.resize((int(my_img4.size[0]*scale), int(my_img4.size[1]*scale)), Image.ANTIALIAS))

my_img5=Image.open("Images/Rory5.png")
my_img5=ImageTk.PhotoImage(my_img5.resize((int(my_img5.size[0]*scale), int(my_img5.size[1]*scale)), Image.ANTIALIAS))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]



status=tk.Label(root,text="Image 1 of {}".format(len(image_list)),bd=1,relief="sunken",anchor="e")
status.grid(row=2,column=0,columnspan=3,sticky="w,e")

my_label=tk.Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

button_back=tk.Button(root,text="<<",command=lambda: back,state="disabled")

button_forward=tk.Button(root,text=">>",command=lambda: forward(2))
button_quit= tk.Button(root,text="Exit Program",command=lambda: root.destroy())

button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2,pady=10)
button_quit.grid(row=1,column=1)

def forward(image_number):

    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label=tk.Label(image=image_list[image_number-1])

    button_forward=tk.Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back=tk.Button(root,text="<<",command=lambda: back(image_number-1))
    
    if image_number==len(image_list):
        button_forward=tk.Button(root,text=">>",state="disabled")


    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    my_label.grid(row=0,column=0,columnspan=3)


    status=tk.Label(root,text="Image {} of {}".format(image_number,len(image_list)),bd=1,relief="sunken",anchor="e")
    status.grid(row=2,column=0,columnspan=3,sticky="w,e")
def back(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label=tk.Label(image=image_list[image_number-1])

    button_forward=tk.Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back=tk.Button(root,text="<<",command=lambda: back(image_number-1))

    if image_number==1:
        button_back=tk.Button(root,text="<<",state="disabled")

    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    my_label.grid(row=0,column=0,columnspan=3)

    status=tk.Label(root,text="Image {} of {}".format(image_number,len(image_list)),bd=1,relief="sunken",anchor="e")
    status.grid(row=2,column=0,columnspan=3,sticky="w,e")

root.mainloop()
