from tkinter import *
def ham(event):
    print(f"Clicked at {event.x}, {event.y}")
def hamm(event):
    print("Yess")
def hammm(event):
    print("Clicked on Canvas")
root=Tk()
root.geometry("800x400")
can_widget = Canvas(root, width=800, height=400)
can_widget.pack()
can_widget.create_line(0,0,800,400)
can_widget.create_rectangle(100,100,400,300,fill="red")
can_widget.create_oval(100,100,400,300,fill="blue")
can_widget.create_line(0,400,800,0,fill="blue")
can_widget.create_text(250,200,text="Hamdan",font="Georgia 50 italic",fill="yellow")
b = Button(root, text="Submit")
b.pack()
b.bind('<Button-1>', ham)
b.bind('<Button-3>', hamm)
can_widget.bind('<Button-2>', hammm)

root.mainloop()