import random
import turtle


def branch():
    turtle.forward(arm_len)
    for i in range(3):
        turtle.left(angle / 2)
        for j in range(3):
            turtle.forward(branch_len)
            turtle.backward(branch_len)
            turtle.right(angle / 2)
        turtle.left(angle)
        turtle.backward(arm_len / 3)


turtle.delay(0)
turtle.bgcolor("black")
turtle.color("white")
turtle.width(random.randint(2, 8))

arm_len = random.randint(90, 140)
branch_len = random.randint(20, 80)
angle = random.randint(90, 180)

for i in range(6):
    branch()
    turtle.right(60)

turtle.done()
