import turtle
from turtle import *
n1="HAMDAN";n2="";n3="";n4=""

win=turtle.Screen()
win.title("Ludo by HAMDAN")
win.setup(width=999, height=600)
win.bgcolor("light blue")
win.bgpic("board.gif")


pen=turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(-490,150)
pen.write("Leaderboard :-\n\n1st Winner   : \n2nd Winner : \n3rd Winner : \nLoser           :",n1,font=("Comic Sans MS",11,"italic"),align="left")
def window():
    win=turtle.Screen()
    win.title("Ludo by HAMDAN")
    win.setup(width=999, height=600)
    win.bgcolor("light blue")
    win.bgpic("board.gif")

def writes(a,b,c,d):

    pen.clear()
    pen.goto(-490,150)
    pen.write("Leaderboard :-\n\n1st Winner : {}\n2nd Winner :\n3rd Winner :\nLoser :".format(a),n1,font=("Comic Sans MS",11,"italic"),align="left")

die=turtle.Turtle()
die.speed(0)
die.penup()
die.goto(400, -200)
die.color("white")
die.shape("square")
die.shapesize(stretch_wid=4, stretch_len=4)

def roll():
    die.speed(0)
    die.goto(400, -200)
    die.speed(1)
    die.goto(350, -40)
    die.left(180)
    die.goto(395, 140)
    die.left(360)
    number6()


def number6():

    die.hideturtle()
    win.bgpic("n6.gif")


window()
writes(n1,n2,n3,n4)

turtle.listen()
turtle.onkey(roll,'space')


turtle.mainloop()
turtle.done()