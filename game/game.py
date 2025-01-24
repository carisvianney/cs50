import random

#prompt the user for a positive integer 
while True:
    try:
        level = int(input("Level: "))
    except ValueError: pass
    else:
        if not level > 0: pass
        else:
            break

#generate a random integer between 1 and n, inclusive
number = random.randint(1,100)

#Accepting guesses
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError: pass
    else:
        if not guess > 0: pass
        else:
            if guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break