import turtle
#import winsound


#img = "C:/Users/KIIT/Desktop/holi.jpg"
win=turtle.Screen()
win.title("Happy Holi from Hamdan !!!")
win.bgcolor("light blue")
win.setup(width=800, height=600)
win.tracer(0)
k = 1
kk= 0
c = 1

ham = turtle.Turtle()
ham.speed(0)
ham.penup()
ham.goto(300,0)
ham.pendown()
ham.color("black", "orange")
ham.begin_fill()
for i in range(25):
    ham.forward(10)
    ham.left(14.4)
ham.end_fill()
ham.right(90)
ham.forward(50)

ham.right(135)
ham.forward(50)

ham.right(180)
ham.forward(50)

ham.right(150)
ham.forward(50)

ham.right(180)
ham.forward(50)

ham.right(75)
ham.forward(50)

ham.right(45)
ham.forward(50)

ham.right(180)
ham.forward(50)

ham.right(90)
ham.forward(50)

ham.hideturtle()




















a = turtle.Turtle()
a.speed(0)
a.shape("circle")
a.color("red")
a.shapesize(stretch_wid=4, stretch_len=4)
a.penup()
a.goto(235, 0)
x=a.xcor()
y=a.ycor()
a.dx = -.35
a.dy =  .45


b = turtle.Turtle()
b.speed(0)
b.shape("circle")
b.color("blue")
b.shapesize(stretch_wid=.0001, stretch_len=.0001)
b.penup()
b.goto(-30, 180)

c = turtle.Turtle()
c.speed(0)
c.shape("square")
#c.color("blue")
c.shapesize(stretch_wid=20, stretch_len=.2)
c.penup()
c.goto(-100, 50)

d = turtle.Turtle()
d.speed(0)
d.shape("square")
d.shapesize(stretch_wid=.2, stretch_len=1)
d.penup()
d.goto(-90, 180)

e = turtle.Turtle()
e.speed(0)
e.shape("square")
e.shapesize(stretch_wid=1, stretch_len=10)
e.penup()
e.goto(-100, -150)

r = 0
d = 6.5
net = turtle.Turtle()
net.color("blue")
net.hideturtle()
net.penup()
net.goto(-25,145)
net.width(4)
net.pendown()
net.left(17)
for i in range(9):
    net.left(r)
    net.forward(d)
    r += 2

for i in range(9):
    net.left(r)
    net.forward(d)
    r -= 2

for i in range(9):
    net.left(r)
    net.forward(d)
    r += 2

for i in range(9):
    net.left(r)
    net.forward(d)
    r -= 2
net.left(18)
net.forward(20)

net.color("black")
net.width(3)

net.penup()
net.forward(37)
net.left(90)
net.forward(25)
net.pendown()
net.left(170)
net.forward(80)

net.penup()
net.right(90)
net.forward(25)
net.pendown()
net.right(90)
net.forward(53)

net.penup()
net.left(90)
net.forward(25)
net.left(90)
net.forward(6)

net.pendown()
#net.right(90)
net.forward(53)

net.penup()
net.right(90)
net.forward(25)
net.pendown()
net.right(90)
net.forward(55)







net.penup()
net.forward(6)
net.left(90)
net.forward(15)
net.pendown()
net.left(170)
net.forward(90)



net.penup()
net.right(90)
net.forward(25)
net.left(90)
net.forward(5)
net.right(90)
net.pendown()
net.right(90)
net.forward(80)

net.penup()
net.left(90)
net.forward(20)
net.left(90)
net.forward(6)

net.pendown()
net.forward(53)

net.penup()
net.goto(-77,105)
net.pendown()
net.goto(-81,177)





net.penup()
net.goto(-65,155)
net.pendown()
net.goto(-53,207)


net.penup()
net.goto(-27,207)
net.pendown()
net.goto(-41,147)

net.penup()
net.goto(-17,149)
net.pendown()
net.goto(-5,203)









def leftup():

    a.setx(a.xcor()+a.dx)
    a.sety(a.ycor()+a.dy)








while(True):

    leftup()
    win.update()
    if c==1:
        c+=1
        for i in range(3000000):
            k *= -1

    if a.ycor()>=300:

        a.dy *= -1
    if a.xcor()<=-60:

        a.dx *= -1
        kk=1

    if a.xcor() <= b.xcor() and kk ==1 and a.ycor() <= b.ycor()+5:
        #winsound.PlaySound("App1",winsound.SND_ASYNC)
        a.dx=0
        a.dy *= 1.005

    if a.ycor()+160 <= c.ycor() and kk==1:
        a.dy *= -.8
        kk=2

    elif a.ycor()+60 >= c.ycor() and kk==2:
        a.dy *= -1.1
        kk=3
    elif a.ycor()+160 <= c.ycor() and kk==3:
        break


for i in range(500000):
    k *= -1

win.clear()
win.bgcolor("light blue")
a = turtle.Turtle()
a.speed(0)
a.shape("circle")
a.color("blue")
a.shapesize(stretch_wid=10, stretch_len=10)
a.penup()
a.goto(0, 0)

for i in range(800000):
    k *= -1

win.clear()
win.bgcolor("light blue")
a = turtle.Turtle()
a.speed(0)
a.shape("circle")
a.color("red")
a.shapesize(stretch_wid=20, stretch_len=20)
a.penup()
a.goto(0, 0)

for i in range(800000):
    k *= -1
win.clear()
win.bgcolor("light blue")


pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write("Happy", align="center", font=("Segoe UI Semibold", 48, "italic"))

pen.color("red")
pen.goto(0, -70)
pen.write("Holi", align="center", font=("Segoe UI Semibold", 48, "italic"))

for i in range(5000000):
    k *= -1
win.clear()
win.bgcolor("light blue")

pen.color("red")
pen.goto(0, 45)
pen.write("Let this festival of colours", align="center", font=("Segoe UI Semibold", 24, "italic"))

pen.color("blue")
pen.goto(0, 10)
pen.write("bring a lot of happiness in your life", align="center", font=("Segoe UI Semibold", 24, "italic"))

pen.color("red")
pen.goto(0, -25)
pen.write("and achieve all heights of success. ", align="center", font=("Segoe UI Semibold", 24, "italic"))

pen.color("blue")
pen.goto(0, -140)
pen.write("Wishing you a very happy holi. \n                       ❤", align="center", font=("Segoe UI Semibold", 24, "italic"))

pen.color("black")
pen.goto(0, -250)
pen.write("from : Your @bright_hamdan", align="center", font=("Segoe UI Semibold", 13, "italic"))




#turtle.register_shape(img)
#win.addshape(img)
#turtle.shape(img)

















turtle.done()