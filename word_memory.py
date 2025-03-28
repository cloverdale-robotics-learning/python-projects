import random

words = [
    "apple",
    "cat",
    "dog",
    "elephant",
    "fish",
    "giraffe",
    "horse",
    "iguana",
    "jaguar",
    "kangaroo",
    "lion",
    "monkey",
    "newt",
    "owl",
    "penguin",
]

print("WORD MEMORY GAME")
print("remember the words")
cwords = random.choices(words, k=3)
print(" ".join(cwords))
cont = False
sentence = "whatever"
input("press enter to continue")
print("\n" * 99)
while not cont:
    print("please type: " + sentence)
    if input() == sentence:
        cont = True
        print("OK")
    else:
        print("TRY AGAIN")

score = 0
userwords = input("Now type the original words: ")
uwords = userwords.split()
for word in uwords:
    if word in cwords:
        score += 1

print("Your score is:", score, "out of", len(cwords))

userwords = input("Now type them in the correct order: ")
uwords = userwords.split()
if uwords == cwords:
    score += len(cwords)

print("Your score is:", score, "out of", len(cwords))
