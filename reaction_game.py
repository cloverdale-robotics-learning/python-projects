import random
import time
import turtle


def write(x):
    turtle.clear()
    turtle.write(x, align="center", font=("Arial", 32, "normal"))


def stop():
    end = time.time()
    if 0 < end - start <= 0.4:
        turtle.color("green")
    else:
        turtle.color("red")
    write(round(end - start, 3))


def go():
    turtle.color("green")
    write("GO")


turtle.listen()
turtle.hideturtle()
write("Press SPACE when you see GO")
time.sleep(2)
turtle.clear()
wait = random.randint(3, 6)
start = time.time() + wait
turtle.ontimer(go, wait * 1000)
turtle.onkeypress(stop, "space")
turtle.done()
