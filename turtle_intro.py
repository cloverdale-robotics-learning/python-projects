import random
import turtle as t

t.colormode(255)

while True:
    t.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    for i in range(4):
        t.forward(90)
        t.left(90)
    t.left(5)
