camel_case = input("camelCase: ")

def find_upper(cadena):
    for letter in cadena:
        if letter.isupper():
            return letter
    return None


