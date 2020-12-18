import turtle

win = turtle.Screen()
win.title("Pong by Hamdan")
win.bgcolor("light blue")
win.setup(width=800, height=600)
win.tracer(0)

sa = 0
sb = 0


pa = turtle.Turtle()
pa.speed(0)
pa.shape("square")
pa.color("green")
pa.shapesize(stretch_wid=5, stretch_len=1)
pa.penup()
pa.goto(-350, 0)

pb = turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.color("green")
pb.shapesize(stretch_wid=5, stretch_len=1)
pb.penup()
pb.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)

ball.dx = .2
ball.dy = .2

pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=("Segoe UI Semibold", 24, "italic"))






def paup():
    y = pa.ycor()
    y += 20
    pa.sety(y)

def padown():
    y = pa.ycor()
    y -= 20
    pa.sety(y)

def pbup():
    y = pb.ycor()
    y += 20
    pb.sety(y)

def pbdown():
    y = pb.ycor()
    y -= 20
    pb.sety(y)

def cheat():
    sb.__setattr__(sb, sb+1)




win.listen()
win.onkeypress(paup, "w")
win.onkeypress(padown, "s")
win.onkeypress(pbup, "Up")
win.onkeypress(pbdown, "Down")
win.onkeypress(cheat, "Right")


while(True):
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        sa += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(sa, sb), align="center", font=("Segoe UI Semibold", 24, "italic"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        sb += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(sa, sb), align="center", font=("Segoe UI Semibold", 24, "italic"))

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < pb.ycor() + 50 and ball.ycor() > pb.ycor() -50):
        ball.setx(340)
        ball.dx *= -1


    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < pa.ycor() + 50 and ball.ycor() > pa.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1