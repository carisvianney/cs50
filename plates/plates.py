def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # if .isalpha in s[0:2]:
    for character in s:
        print(character[0])
        # if character[0:2]
        if len(s) <= 6 and len(s) >= 2:
            return True
        else:
            False



main()
