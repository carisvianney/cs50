def main():
    while True:
        fraction_given = input("Fraction: ")
        if not "-" in fraction_given:
            percentage = convert(fraction_given)
            fuel_level = gauge(percentage)

            print(fuel_level)
            break

def convert(fraction):
    numerador, denominador = fraction.split("/")
    try:
        numerador = float(numerador)
        denominador = float(denominador)
    except ValueError:
        return
            
    if numerador.is_integer() and denominador.is_integer():
        if numerador <= denominador:
            percentage = numerador/denominador * 100
            return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()