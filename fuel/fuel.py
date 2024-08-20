# Prompt user in format X/Y where x and y are integers

def main():
    valid = False
    while not valid:
        global fraction_given
        fraction_given = input("Fraction: ")
        if not "-" in fraction_given:
            global numerador, denominador
            numerador, denominador = fraction_given.split("/")
       
            # switch valid = True
            result = validation()
            if result == True:
                break


    percentaje = convert(fraction_given)

    # 1% or less remain outputs E and if 99% or more remains output F to indicate tank is full
    if percentaje <= 1:
        print("E")
        return
    elif percentaje >= 99:
        print("F")
        return

    # Outputs a percentaje of fuel rounded to the nearest integer
    print(round(percentaje), end="")
    print("%")

def convert(fraction):
    number = (float(numerador)/float(denominador)) * 100
    return number


# If x or y not an integer, x is greater than y or y is 0, prompt the user again
def validation(): 
    try:
        if float(numerador).is_integer() and float(denominador).is_integer():
           # if not float(denominador) == 0:
                if  float(numerador) <= float(denominador):
                    return True
    except ValueError:
        print("This is THE ValueError")
    return False

main()
# Catch any exceptions like ValueError or ZeroDivisionError