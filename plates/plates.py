def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if plate[0].isalpha() and plate[1].isalpha():
        if len(plate) <= 6 and len(plate) >= 2:
            return True
        else:
            False

def num_valid(plate):
    # “Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.”
    plate.reverse()
    print(plate)


main()
