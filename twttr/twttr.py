Input = input("Input: ")

def main():
    vowels = ["a", "e", "i", "o", "u"]
    for letter in Input:
        if letter.lower() not in vowels:
            print(letter, end="")
        else:
            print("", end="")


main()
print()
