Input = input("Input: ")

def main():
    vowels = ["a", "e", "i", "o", "u"]
    for letter in list(Input):
        if letter in vowels:
            print("")
        else:
            print(letter, end="")


main()
