camelCase = input("camelCase: ")


for letter in list(camelCase):
    if letter.isupper():
        letter = letter.lower()
    print(letter, end="")

