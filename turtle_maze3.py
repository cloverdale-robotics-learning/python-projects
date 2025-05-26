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

goal = turtle.Turtle()
goal.shape("circle")
goal.color("red")
goal.penup()
goal.goto(0, 0)

walls = []
score = 0


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
                walls.append(((x, y), (x + cell_size, y)))

            if random.choice([True, False]):
                maze_drawer.goto(x, y)
                maze_drawer.setheading(-90)
                maze_drawer.pendown()
                maze_drawer.forward(cell_size)
                maze_drawer.penup()
                walls.append(((x, y), (x, y - cell_size)))
                maze_drawer.setheading(0)


def is_collision(new_x, new_y):
    for wall in walls:
        (x1, y1), (x2, y2) = wall
        if (x1 == x2 == new_x and y2 <= new_y <= y1) or (y1 == y2 == new_y and x1 <= new_x <= x2):
            return True
    return False


def check_goal():
    if player.distance(goal) < 35:
        global score
        score += 1
        maze_drawer.clear()
        maze_drawer.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
        walls.clear()
        player.goto(-200, 200)
        draw_maze()


def move_up():
    x, y = player.pos()
    y += 20
    if not is_collision(x, y):
        player.goto(x, y)
        check_goal()


def move_down():
    x, y = player.pos()
    y -= 20
    if not is_collision(x, y):
        player.goto(x, y)
        check_goal()


def move_left():
    x, y = player.pos()
    x -= 20
    if not is_collision(x, y):
        player.goto(x, y)
        check_goal()


def move_right():
    x, y = player.pos()
    x += 20
    if not is_collision(x, y):
        player.goto(x, y)
        check_goal()


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

draw_maze()

screen.mainloop()
