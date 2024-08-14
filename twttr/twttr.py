Input = input("Input: ")

def main():
    vowels = ["a", "e", "i", "o", "u"]
    for letter in Input:
        while letter not in vowels:
            print(letter, end="")


main()
print()
