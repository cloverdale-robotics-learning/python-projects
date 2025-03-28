def scramble(text, key):
    scrambled = ""
    for letter in text:
        shifted = (ord(letter) - 32 + key) % 95 + 32
        scrambled += chr(shifted)
    return scrambled


mode = input("Scramble or unscramble? (s/u): ")
text = input("Enter message: ")
key = int(input("Enter key number: "))
if mode == "s":
    print(scramble(text, key))
else:
    print(scramble(text, -key))
