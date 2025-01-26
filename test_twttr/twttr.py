def main():
    Input = input("Input: ")
    print(shorten(Input))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    shorted = []
    for letter in word:
        if letter.lower() not in vowels:
            shorted.append(letter)
            #print(letter, end="")
        else:
            pass
            #print("", end="")
    return "".join(shorted)


if __name__ == "__main__":
    main()
