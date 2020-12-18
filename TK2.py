



'''from tkinter import *
root = Tk()
root.geometry("655x333")
root.minsize(160,120)
f1 = Frame(root, bg="blue", borderwidth=6,
           relief=RAISED)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, borderwidth=8, bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill=X)

l = Label(f1, text="Project Tkinter - PyCharm",
          font="Arial 16 bold", fg="red ")
l.pack(pady=42)

l = Label(f2, text="Welcome to Sublime text")
l.pack()

root.mainloop()


'''

















'''





from tkinter import *
root = Tk()
root.geometry("655x333")
root.minsize(160,120)


f1 = Frame(root, bg="blue", borderwidth=6,
           relief=RAISED)
f1.pack(side=LEFT, anchor="nw")

def hello():
    b3 = Button(f1, fg="red", text="Print now")
    b3.pack(side=LEFT)

b1 = Button(f1, fg="red", text="Print now")
b1.pack(side=LEFT)

b2 = Button(f1, fg="red", text="Print now", command=hello)
b2.pack(side=LEFT,padx=25)

root.mainloop()





'''













from tkinter import *
root = Tk()
root.geometry("655x333")
root.minsize(160,120)

def getvals():
    p = ''
    for i in range(len(passval.get())):
        p = p+'*'
    if userval.get() != "" or passval.get() != "":
        Label(root, text="User = "+userval.get()).grid()
        Label(root, text="Pass = "+p).grid()
        Label(root, text=custval.get()).grid()
        with open("name.txt",'a') as f:
            f.write("\nUser = "+userval.get()+" ")
            f.write("Pass = "+p+" ")
            f.write(str(custval.get())+" ")
        userval.set("")
        passval.set("")
        custval.set(0)

user = Label(root, text="Username")
password = Label(root, text="Password")
newcust = Label(root, text="Already a Customer")
user.grid()
password.grid(column=20)
newcust.grid(row=4, column=10)

userval = StringVar()
passval = StringVar()
custval = IntVar()

userentry = Entry(root, textvariable = userval)
passentry = Entry(root, textvariable = passval)
passentry.config(show="*")
custal = Checkbutton(text="Already booked ? ",variable=custval)
custal.grid(row=4, column=20)


userentry.grid(row=0, column=1)
passentry.grid(row=1, column=21)

Button(text="Submit", command=getvals).grid(row=2, column=25)

root.mainloop()












































































