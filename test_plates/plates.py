def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    plate_list = list(plate)
    long = len(plate_list)
    # debe ser mayor a 2 y menor que 6
    if len(plate) < 2 or len(plate) > 6:
        return False

    # los dos primeros char deben ser letras
    if plate[0].isdigit() or plate[1].isdigit():
        return False



    # a partir del primer numero, no debe haber letras
    num_section = False
    for char in plate:
        if not num_section and char.isdigit():
            if char == '0':
                return False
            num_section = True

        if num_section and char.isalpha():
            return False

        # no puede incluir signos de puntuacion
        if not char.isalnum():
            return False
    return True


"""
    “Numbers cannot be used in the middle of a plate; they must come at the end.
    For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    The first number used cannot be a ‘0’.”
"""

"""
def num_valid(plate):
   if len(plate) > 3:
       if plate[2] != 0:
           return True
       else:
           False
"""

if __name__ == "__main__":
    main()
