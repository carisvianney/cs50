camelCase = input("camelCase: ")


for letter in list(camelCase):
    if letter.isupper():
        letter = letter.lower()
        print("_", letter)
    print(letter, end="")

