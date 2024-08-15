def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    plate_list = list(plate)
    long = len(plate_list)
    print(plate_list)

    #validación del tamaño
    if len(plate) <= 6 and len(plate) >= 2:

        #validación de dos primeros chars como letras
        if plate[0].isalpha() and plate[1].isalpha():

            #Requisitos por tamaño
            while long <= 6 and long >= 2:
                

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
