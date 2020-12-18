
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("644x970")
root.title("Calculator By HAMDAN")
root.wm_iconbitmap("icon.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=6, padx=6)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=28, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=28, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=28, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="6", padx=28, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=28, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=28, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="3", padx=28, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=28, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=28, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="0", padx=30, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=30, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=30, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="/", padx=31, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=29, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=27, pady=15, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="C", padx=36.2, pady=5, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=41, pady=5, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=31, pady=5, font="lucida 15 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()
