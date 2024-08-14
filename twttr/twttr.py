Input = input("Input: ")

def main():
    vowels = ["a", "e", "i", "o", "u"]
    for letter in Input:
        if letter.isupper():
            if letter in vowels:
                print("", end="")
        elif letter in vowels:
                print("", end="")
        else:
            print(letter, end="")

main()
print()
