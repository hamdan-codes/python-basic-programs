import turtle
import random

c=0
kk=1
n=int(input("Enter size : "))

win = turtle.Screen()
win.title("Parking Lot KIIT")
win.bgcolor("light blue")
win.setup(width=800, height=600)
win.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(-50, -100)

ar=[]
for i in range(n):
    ar.append(0)
def ci():
    m=0
    for i in range(n):
        if int(ar[i])==0:
            ar[i]=1
            m=i
            break
    c=m
    display()
    pen.pendown()
    pen.write("Came in: {}".format(c), align="center", font=("Segoe UI Semibold", 24, "italic"))




    return c



def go(i):
    if ar[i] == 0 and i !=0:
        i=i-1
    ar[i]=0
    display()
    pen.pendown()


    pen.write("Went out: {}".format(i), align="center", font=("Segoe UI Semibold", 24, "italic"))





def check(i):
    if int(ar[i])==0:
        return 0
    else:
        return 1







def display():



    lots = turtle.Turtle()
    lots.width(50)
    lots.hideturtle()
    lots.speed(0)
    lots.shape("circle")
    lots.shapesize(stretch_wid=5, stretch_len=5)
    lots.penup()
    lots.goto(-400, 0)
    lots.pendown()
    for i in range(n):
        if int(check(i))==0:
            lots.color("yellow")
        elif int(check(i))==1:
            lots.color("red")
        if i==0:
            lots.color("red")
        lots.penup()
        lots.forward(50)
        lots.speed(0)
        lots.pendown()
        lots.forward(5)



    '''for i in range(n):
        lot[i]=turtle.Turtle()
        lot[i].penup()
        lot[i].speed(0)
        lot[i].goto(0,0)
        lot[i].pendown()
        lot[i].forward(10)'''



















k=1
for i in range(80000):
    k=k*-1

while True:
    if ar[n-1]==1:
        break
    win.clear()
    win.title("Parking Lot KIIT")
    win.bgcolor("light blue")
    win.setup(width=800, height=600)
    win.update()
    x=random.randint(1,2)

    if x==1:
        xx=ci()
        pen.pendown()
        pen.write("Came in: {}".format(xx), align="center", font=("Segoe UI Semibold", 24, "italic"))

    else:
        s=random.randint(0,xx)
        go(s)
        pen.pendown()
        pen.write("Went out: {}".format(s), align="center", font=("Segoe UI Semibold", 24, "italic"))

turtle.mainloop()
turtle.done()


