from tkinter import *
from playsound import playsound
root = Tk()
root.geometry("700x323")
root.minsize(width=700, height=323)
root.maxsize(width=700, height=323)
root.title("My MusicPlayer | @bright_hamdan")
root.wm_iconbitmap("icon.ico")

def play():
    playsound(f"{userval.get()}.wav")
    root.update()
    root.mainloop()

Label(root,text="Welcome to MusicPlayer by Hamdan",font="lucida 30 italic",pady=20).grid(row=1,column=1)

Label(root,text="Song name           :-- ").grid(row=2,column=1)
userval = StringVar()
userentry = Entry(root, textvariable = userval)
userentry.grid(row=3, column=1)


Button(text="   | >  ", command=play).grid(row=4, column=1)
Button(text="   | |   ").grid(row=5, column=1)
Button(text="    <  ").grid(row=6, column=1)
Button(text="    >  ").grid(row=7, column=1)
Button(text="    <<  ").grid(row=8, column=1)
Button(text="    >>  ").grid(row=9, column=1)
root.mainloop()

