def scramble(text, key):
    scrambled = ""
    for letter in text:
        shifted = (ord(letter) - 32 + key) % 95 + 32
        scrambled += chr(shifted)
    return scrambled


text = input("Enter scrambled message: ")
for key in range(95):
    print(scramble(text, -key))
