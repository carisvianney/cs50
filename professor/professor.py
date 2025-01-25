import random

def main():
    global level
    level = get_level()
    levels = 10
    score = 0

    while True:
        if problem() == 1:
            score = score + 1
        else: pass

        levels = levels - 1
        if levels == 0:
            print(f"Score: {score}")
            break

    
def get_level():
    #prompt the user for a level [1,3]
    while True:
        level = input("Level: ")
        try:
            if int(level):
                level = int(level) 
                if 3 >= level >= 1: 
                    return level
        except ValueError: pass
            
def generate_integer(level):
    if level == 1:
        integer = random.randint(0, 9)
    elif level == 2:
        integer = random.randint(10, 99)
    else:
        integer = random.randint(100,999)
    return integer

def problem():
    x = generate_integer(level)
    y = generate_integer(level)
    answer = x + y
    attempts = 3

    while True:
        try:
            user_answer = int(input(f"{x} + {y} = "))
        except ValueError: pass 

        if user_answer == answer:
            return 1
        else:
            print("EEE")

        attempts = attempts -1
        if attempts == 0:
            print(f"{x} + {y} = {answer}")
            break


if __name__ == "__main__":
    main()
