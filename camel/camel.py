camel_case = input("camelCase: ")

def find_upper(cadena):
    for letter in cadena:
        if letter.isupper():
            return "_" + letter

find_upper(camel_case)
