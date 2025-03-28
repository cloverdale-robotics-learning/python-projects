import random

words = ["apple", "banana", "grape", "orange", "strawberry"]
word = random.choice(words)
letters = list(word)
tries = 6
guessed = list("_" * len(word))
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word: " + " ".join(guessed))

while tries > 0:
    guess = input("\nEnter a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
    elif guess in letters:
        for i in range(len(letters)):
            if letters[i] == guess:
                guessed[i] = guess
        guessed_letters.append(guess)
    else:
        tries -= 1
        guessed_letters.append(guess)
        print(f"Wrong guess! You have {tries} attempts left.")

    print(" ".join(guessed))

    if "_" not in guessed:
        print("\nCongratulations! You've guessed the word!")
        break
else:
    print("\nYou've run out of attempts! The word was '" + word + "'.")
