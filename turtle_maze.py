import random
import turtle

screen = turtle.Screen()

maze_drawer = turtle.Turtle()
maze_drawer.speed(0)
maze_drawer.penup()
maze_drawer.hideturtle()

player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)
player.goto(-200, 200)


def draw_maze():
    start_x, start_y = -200, 200
    cell_size = 40
    maze_drawer.goto(start_x, start_y)

    for i in range(10):
        for j in range(10):
            x = start_x + j * cell_size
            y = start_y - i * cell_size
            maze_drawer.goto(x, y)

            if random.choice([True, False]):
                maze_drawer.pendown()
                maze_drawer.forward(cell_size)
                maze_drawer.penup()

            if random.choice([True, False]):
                maze_drawer.goto(x, y)
                maze_drawer.setheading(-90)
                maze_drawer.pendown()
                maze_drawer.forward(cell_size)
                maze_drawer.penup()
                maze_drawer.setheading(0)


def move_up():
    x, y = player.pos()
    player.goto(x, y + 20)


def move_down():
    x, y = player.pos()
    player.goto(x, y - 20)


def move_left():
    x, y = player.pos()
    player.goto(x - 20, y)


def move_right():
    x, y = player.pos()
    player.goto(x + 20, y)


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

draw_maze()

screen.mainloop()
