camelCase = input("camelCase: ")


for letter in camelCase:
    if letter.isupper():
        letter = "_" + letter.lower()
    print(letter, end="")

print()

