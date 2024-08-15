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
    # index comienza en cero
    i = 0
    for index, char in enumerate(plate):
        # se itera cada caracter del plate
        if char.isdigit():
            # si es digito, se sale del loop con el index del digito
            i = index
            break

    nums = plate[i, len(plate)]
    if 

    # Requisitos por tamaño

    while long <= 6 and long >= 2:
        for n in plate:
            if plate[n].isalpha():
                print(n)
                return True
            else:
                False


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

main()
