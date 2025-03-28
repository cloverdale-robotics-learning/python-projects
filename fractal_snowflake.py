import turtle


def draw_snowflake_side(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        for a in [0, 60, -120, 60]:
            turtle.left(a)
            draw_snowflake_side(length, depth - 1)


def draw_snowflake(length, depth):
    for i in range(6):
        draw_snowflake_side(length, depth)
        turtle.right(60)


turtle.bgcolor("black")
turtle.color("white")
turtle.hideturtle()
turtle.speed(0)
turtle.delay(0)
turtle.penup()
turtle.goto(-150, 250)
turtle.pendown()

draw_snowflake(300, 4)
turtle.done()
