from tkinter import *
root=Tk()
root.geometry("800x400")
can_widget = Canvas(root, width=800, height=400)
can_widget.pack()
can_widget.create_line(0,0,800,400)
can_widget.create_rectangle(100,100,400,200,fill="red")
can_widget.create_line(0,400,800,0)


root.mainloop()