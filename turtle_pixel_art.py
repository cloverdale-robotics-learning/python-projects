import time
import turtle

rows = 20
cols = 20
pixel_size = 20

turtle.speed(0)
turtle.colormode(1.0)
turtle.shape("square")
turtle.shapesize(pixel_size / 20)
turtle.penup()

start_x = -cols * pixel_size // 2
start_y = rows * pixel_size // 2

for row in range(rows):
    for col in range(cols):
        t = time.time()
        r = (row / rows + t) % 1
        g = (col / cols + t) % 1
        b = ((row + col) / (rows + cols) + t) % 1
        color = (r, g, b)
        turtle.color(color)

        x = start_x + col * pixel_size
        y = start_y - row * pixel_size
        turtle.goto(x, y)
        turtle.stamp()

turtle.done()
