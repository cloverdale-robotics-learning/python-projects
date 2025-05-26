import random
import turtle

WIDTH = 800
HEIGHT = 600
CELL_SIZE = 10
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE


def next_cell_state(row, col):
    neighbors = 0
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0:
                continue
            try:
                neighbors += grid[row + x][col + y]
            except IndexError:
                continue
    if grid[row][col]:
        return 2 <= neighbors <= 3
    return neighbors == 3


def draw_grid():
    turtle.clear()
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col]:
                x = -WIDTH // 2 + col * CELL_SIZE
                y = HEIGHT // 2 - row * CELL_SIZE
                turtle.goto(x, y)
                turtle.stamp()


turtle.setup(WIDTH, HEIGHT)
turtle.tracer(0)
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.shape("square")
turtle.shapesize(CELL_SIZE / 20)
turtle.bgcolor("gray20")
turtle.color("yellow")

grid = [[random.choice([0, 1]) for col in range(COLS)] for row in range(ROWS)]

while True:
    draw_grid()
    grid = [[next_cell_state(row, col) for col in range(COLS)] for row in range(ROWS)]
    turtle.update()
