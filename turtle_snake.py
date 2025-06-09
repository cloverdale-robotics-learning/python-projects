import turtle
import time
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(600, 600)
wn.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 60)

segments = []
direction = "stop"

def go_up():
    global direction
    if direction != "down":
        direction = "up"
def go_down():
    global direction
    if direction != "up":
        direction = "down"
def go_left():
    global direction
    if direction != "right":
        direction = "left"
def go_right():
    global direction
    if direction != "left":
        direction = "right"

def move():
    if direction == "up":
        head.sety(head.ycor() + 20)
    if direction == "down":
        head.sety(head.ycor() - 20)
    if direction == "right":
        head.setx(head.xcor() + 20)
    if direction == "left":
        head.setx(head.xcor() - 20)

wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

def restart():
    global direction, segments
    time.sleep(1)
    head.goto(0, 0)
    direction = "stop"
    for segment in segments:
        segment.hideturtle()
    segments.clear()
    food.goto(0, 60)

while True:
    wn.update()

    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        restart()

    if head.distance(food) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            restart()

    time.sleep(0.1)
