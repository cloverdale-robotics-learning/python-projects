import random
import turtle


def draw_tree(length, depth):
    if depth > 0:
        angle = random.randint(20, 40)
        cut = random.uniform(0.5, 0.8)
        turtle.forward(length)
        turtle.left(angle)
        draw_tree(length * cut, depth - 1)
        turtle.right(angle * 2)
        draw_tree(length * cut, depth - 1)
        turtle.left(angle)
        turtle.back(length)


turtle.delay(0)
turtle.left(90)
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()

draw_tree(150, 8)
turtle.done()
