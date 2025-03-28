import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)


def set_color(color):
    return lambda: pen.color(color)


def move_to(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


screen = turtle.Screen()
screen.listen()
screen.onkey(set_color("red"), "r")
screen.onkey(set_color("green"), "g")
screen.onkey(set_color("blue"), "b")
screen.onkey(set_color("yellow"), "y")
screen.onkey(set_color("black"), "k")
screen.onkey(pen.clear, "c")
screen.onclick(move_to, 3)
pen.ondrag(pen.goto)

turtle.done()
