from tkinter import *
import tkinter.messagebox as tmsg
c=0
d=0
root = Tk()
root.geometry("455x344")
root.title("Hamdan's GUI")
root.wm_iconbitmap("icon.ico")
def func():
    global c
    c += 1
    if c==1:
        Label(root,text="Clicked "+str(c)+" time").pack()
    else:
        Label(root, text="Clicked " + str(c) + " times").pack()

def fun():
    global d
    d += 1
    if d == 1:
        Label(root,text="Saved "+str(d)+" time").pack()
    else:
        Label(root, text="Saved " + str(d) + " times").pack()

def funcc():
    a = tmsg.askquestion("Exit", "Are you sure to exit ?")
    if a=='yes':
        #quit()
        root.destroy()


"""menuu = Menu(root)
menuu.add_command(label="File", command=func)
menuu.add_command(label="Exit", command=quit)
root.config(menu=menuu)"""


menuuu = Menu(root)
m1 = Menu(menuuu)
m1.add_command(label="New", command=func)
m1.add_command(label="Save", command=fun)
m1.add_separator()
m1.add_command(label="Exit", command=funcc)
root.config(menu=menuuu)
menuuu.add_cascade(label="File",menu=m1)


m2 = Menu(menuuu,tearoff=0)
m2.add_command(label="Cut", command=func)
m2.add_command(label="Copy", command=func)
m2.add_command(label="Paste", command=func)
root.config(menu=menuuu)
menuuu.add_cascade(label="Edit",menu=m2)

def rev():
    Label(root,text=slider.get()).pack(side=LEFT,padx=10)

Label(root, text="How staisfied are you with our app...?").pack()
slider = Scale(root, from_=0, to=100, orient=HORIZONTAL,length=200,tickinterval=10,font="comicsansms 8")
slider.set(50)
slider.pack()
Button(root,text="Submit Review ...",command=rev).pack()
var=0
radio = Radiobutton(root, text="Samosa", padx=14, variable=var, value=1).pack()
radio = Radiobutton(root, text="Aaloo", padx=14, variable=var, value=2).pack()
radio = Radiobutton(root, text="Gujhiya", padx=14, variable=var, value=3).pack()
radio = Radiobutton(root, text="Chhola", padx=14, variable=var, value=4).pack()

scrlbar = Scrollbar(root)
scrlbar.pack(side=RIGHT, fill=Y)



lb = Listbox(root,yscrollcommand = scrlbar.set)
lb.insert(END,"First Entry")
lb.insert(END,"Second Entry")
lb.insert(END,"First Entry")
lb.insert(END,"Second Entry")
lb.insert(END,"First Entry")
lb.insert(END,"Second Entry")
lb.insert(END,"First Entry")
lb.insert(END,"Second Entry")
lb.insert(END,"First Entry")
lb.insert(END,"Second Entry")
lb.insert(END,"First Entry")
lb.insert(END,"Second Entry")
lb.insert(END,"First Entry")
lb.insert(END,"Second Entry")
lb.insert(END,"First Entry")
lb.insert(END,"Second Entry")
lb.insert(END,"First Entry")
lb.insert(END,"Second Entry")
lb.insert(END,"First Entry")
lb.insert(END,"Second Entry")


lb.pack(fill="both")

scrlbar.config(command=lb.yview)




root.mainloop()

