from tkinter import *
import turtle
import tkinter.messagebox as tmsg
import string
root = Tk()
root.geometry("434x312")
root.title("My own software | @bright_hamdan")
root.wm_iconbitmap("icon.ico")


def log():
    Label(root, text="-------------------", font="lucida 20", pady=5).grid(row=6, column=1)
    root.update()
    c=0
    d=0
    f = open("details.ch","r")
    for line in f:
        for part in line.split():
            if (f"{userval.get()}-") in part and userval.get() != '':
                pw = part[part.find('-')+1:len(part)]
                if pw == passval.get():
                    Label(root, text="Login Success", font="lucida 19", pady=5).grid(row=6, column=1)
                    c=1
                    d=1
                    break
                d=1
        if c==1:
            break
    if d==0 :
        tmsg.showinfo("Login Error", "Username not found. Please signup first. :)")
    elif c==0:
        tmsg.showinfo("Login Error", "Incorrect Password. Please try again. :)")

    f.close()

def sign():
    Label(root, text="-------------------", font="lucida 20", pady=5).grid(row=6, column=1)
    root.update()
    f = open("details.ch","a")
    f.write(f"{userval.get()}-{passval.get()}\n")
    tmsg.showinfo("Signup Success", "Signup Success. Now Login to enter. :)")
    f.close()


Label(root,text="Login/Signup Page",font="lucida 30 italic",pady=20).grid(row=1,column=1)

Label(root,text="User          : ").grid(row=2,column=0)
userval = StringVar()
userentry = Entry(root, textvariable = userval)
userentry.grid(row=2, column=1)
Label(root,text="Password : ").grid(row=3,column=0)
passval = StringVar()
passentry = Entry(root, textvariable = passval)
passentry.config(show="*")
passentry.grid(row=3, column=1)
Button(text="Login   ", command=log).grid(row=4, column=1)
Button(text="Signup ", command=sign).grid(row=5, column=1)





root.mainloop()
