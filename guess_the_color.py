import random

colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128),
    "orange": (255, 165, 0),
    "pink": (255, 192, 203),
}

colorname, rgb = random.choice(list(colors.items()))
print("Guess the color! RGB value:", rgb)
guess = input("Enter the color name: ").strip().lower()
if guess == colorname:
    print("Correct! Well done!")
else:
    print("Oops! The correct color was", colorname)
