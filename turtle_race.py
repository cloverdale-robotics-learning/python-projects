import random
import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
colors = ["red", "blue", "green", "yellow", "purple"]
racers = []
start_x = -200
start_y = 125

track_drawer = turtle.Turtle()
track_drawer.speed(0)
track_drawer.penup()
track_drawer.goto(-200, 150)
for lane in range(len(colors)):
    track_drawer.write(lane, align="center")
    track_drawer.pendown()
    track_drawer.forward(400)
    track_drawer.penup()
    track_drawer.backward(400)
    track_drawer.right(90)
    track_drawer.forward(50)
    track_drawer.left(90)
track_drawer.hideturtle()

for color in colors:
    racer = turtle.Turtle()
    racer.color(color)
    racer.shape("turtle")
    racer.penup()
    racer.goto(start_x, start_y)
    racer.pendown()
    racers.append(racer)
    start_y -= 50

running = True
while running:
    for racer in racers:
        racer.forward(random.randint(1, 10))
        if racer.xcor() >= 200:
            running = False
            winner_color = racer.color()[0]
            track_drawer.goto(0, -200)
            track_drawer.write(f"{winner_color} turtle wins!", align="center", font=("Arial", 16, "bold"))
            break

screen.mainloop()
