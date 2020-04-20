import tkinter as tk
#from PIL import ImageTk,Image

button_font="Calibri 12"
entry_font="Calibri 20"
background_colour="#1f1f1f"
button_colour="#060606"
command_colour="#131313"
interpadding=2
buttonx=30

root = tk.Tk()
root.config(bg="#1f1f1f")
root.title("Calculator")
root.resizable(False,False)
root.iconbitmap("Images/Calculator.ico")
#icon=Image.open("Images/Calculator.png")
#root.iconphoto(False, ImageTk.PhotoImage(icon))

e=tk.Entry(root,bg=background_colour,fg="White",borderwidth=0,font=("Calibri 20"),justify="right",insertbackground=background_colour)
e.grid(row=0,column=0,sticky="ew",columnspan=4,padx=10,pady=10)

def button_click(number):
    current=e.get()
    current=current.replace(",","")
    e.delete(0,"end")
    e.insert(0,"{:,}".format(int((str(current)+str(number)))))

    
def button_clear():
    e.delete(0,"end")


def button_equal():
    second_number=e.get()
    second_number=second_number.replace(",","")
    second_number=float(second_number)
    e.delete(0,"end")

    if math=="addition":
        answer=f_num+second_number
        if str(answer)[-2:]==".0":
            answer=int(answer)
        e.insert(0,"{:,}".format(answer))

    if math=="subtraction":
        answer=f_num-second_number
        if str(answer)[-2:]==".0":
            answer=int(answer)
        e.insert(0,"{:,}".format(answer))

    if math=="multiplication":
        answer=f_num*second_number
        if str(answer)[-2:]==".0":
            answer=int(answer)
        e.insert(0,"{:,}".format(answer)) 

    if math=="division":
        answer=f_num/second_number
        if str(answer)[-2:]==".0":
            answer=int(answer)
        e.insert(0,"{:,}".format(answer))

def button_addition():
    first_number=e.get()
    first_number=first_number.replace(",","")
    global f_num
    global math
    math="addition"
    f_num=float(first_number)
    e.delete(0,"end")

def button_subtract():
    first_number=e.get()
    first_number=first_number.replace(",","")
    global f_num
    global math
    math="subtraction"
    f_num=float(first_number)
    e.delete(0,"end")

def button_multiply():
    first_number=e.get()
    first_number=first_number.replace(",","")
    global f_num
    global math
    math="multiplication"
    f_num=float(first_number)
    e.delete(0,"end")

def button_divide():
    first_number=e.get()
    first_number=first_number.replace(",","")
    global f_num
    global math
    math="division"
    f_num=float(first_number)
    e.delete(0,"end")

button_1=tk.Button(root,text="1",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=lambda: button_click(1))
button_2=tk.Button(root,text="2",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=lambda: button_click(2))
button_3=tk.Button(root,text="3",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=lambda: button_click(3))

button_4=tk.Button(root,text="4",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=lambda: button_click(4))
button_5=tk.Button(root,text="5",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=lambda: button_click(5))
button_6=tk.Button(root,text="6",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=lambda: button_click(6))

button_7=tk.Button(root,text="7",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=lambda: button_click(7))
button_8=tk.Button(root,text="8",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=lambda: button_click(8))
button_9=tk.Button(root,text="9",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=lambda: button_click(9))

button_0=tk.Button(root,text="0",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=lambda: button_click(0))
button_equal=tk.Button(root,text="=",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=button_equal)
button_clear=tk.Button(root,text="Clear",bg=button_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx-13,pady=20,command=button_clear)

button_add=tk.Button(root,text="+",bg=command_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx-1,pady=20, command=button_addition)
button_subtract=tk.Button(root,text="-",bg=command_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx+1,pady=20, command=button_subtract)
button_multiply=tk.Button(root,text="x",bg=command_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=button_multiply)
button_divide=tk.Button(root,text="/",bg=command_colour,fg="White",font=button_font,borderwidth=0,padx=buttonx,pady=20,command=button_divide)


button_1.grid(row=3,column=0,pady=interpadding)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0,pady=interpadding)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0,pady=interpadding)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=1,pady=interpadding)
button_clear.grid(row=4,column=0)
button_add.grid(row=3,column=3)
button_equal.grid(row=4,column=2)

button_subtract.grid(row=4,column=3)
button_multiply.grid(row=1,column=3)
button_divide.grid(row=2,column=3)



root.mainloop()