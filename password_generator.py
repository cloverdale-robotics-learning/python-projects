import random
import string


def generate_password(length, include_special_chars, include_digits):
    chars = string.ascii_letters
    if include_special_chars:
        chars += string.punctuation
    if include_digits:
        chars += string.digits

    password = "".join(random.choices(chars, k=length))
    return password


print("Welcome to the Password Generator!")

while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        break
    except ValueError:
        print("Please enter a valid number for the length.")

include_special_chars = input("Include special characters (yes or no)? ").lower() in ["yes", "y"]
include_digits = input("Include digits (yes or no)? ").lower() in ["yes", "y"]

password = generate_password(length, include_special_chars, include_digits)
print("Your generated password is:", password)
