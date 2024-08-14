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
    

main()
