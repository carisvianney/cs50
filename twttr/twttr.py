Input = input("Input: ")

def main():
    vowels = ["a", "e", "i", "o", "u"]
    for letter in Input:
        if letter.isupper():
            if letter not in vowels:
                print(letter, end="")

        elif letter not in vowels:
            print(letter, end="")
            

main()
print()
