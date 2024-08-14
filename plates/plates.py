def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # if .isalpha in s[0:2]:

    for character in plate:
        print(character[0])

        # if character[0:2]
        
        if len(plate) <= 6 and len(plate) >= 2:
            return True
        else:
            False



main()
