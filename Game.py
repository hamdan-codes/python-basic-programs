import turtle

TURTLE_SIZE = 20  # This is the default for a `square` turtle
SQUARE_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'normal')


def toggle(box):
    """Toggles the colour of a Turtle when it is clicked."""
    if box.color()[0] == "Red":
        box.color("Green")
    else:
        box.color("Red")

# Screen setup
screen = turtle.Screen()
screen.setup(600, 200)
screen.title("The 21 Game")
screen.bgcolor("black")
# Disable animation
screen.tracer(0)

# Create 21 clickable squares
for i in range(21):
    box = turtle.Turtle("square")

    def click_callback(x, y, box=box):
        """Passes `box` to `toggle()` function."""
        return toggle(box)

    box.shapesize(SQUARE_SIZE / TURTLE_SIZE)
    box.color("Red")
    box.penup()
    box.goto(-231 + i * (SQUARE_SIZE + 2), 0)
    box.onclick(click_callback)

# Write numbers above the squares
pen = turtle.Turtle(visible=False)
pen.color("white")
pen.penup()
pen.goto(-231, 22)
for i in range(21):
    pen.write(str(i + 1), align="center", font=FONT)
    pen.forward(22)

# Restore animation
screen.tracer(1)
turtle.done()