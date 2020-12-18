


from tkinter import *
#from PIL import Image, ImageTk
root = Tk()

root.geometry("450x450")
root.minsize(200,100)
root.maxsize(900,600)
root.title("My GUI with Hamdan")

'''
image = Image.open("n6.jpeg")
photo = ImageTk.PhotoImage(image)

'''

photo = PhotoImage(file= "board.gif")
hamm = Label(text = "This is my GUI")
ham = Label(text = "PyCharm")
label = Label(image=photo)
hamm.pack()
ham.pack()

textx = Label(text='''Hey !!!
This is Hamdan.
Want to become a great coder.
Always busy in the practice.
Thank Youuu !!! ''',
bg="red", fg="blue", font="Arial 13 italic",
padx=23, pady=44, borderwidth=5,relief=RAISED)

# textx.pack(side=BOTTOM, anchor="se",fill=X)
textx.pack(side=RIGHT, anchor="se",fill=Y)
#label.pack()









root.mainloop()




