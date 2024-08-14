camel_case = input("camelCase: ")

def find_upper(cadena):
    for letter in cadena:
        if letter.isupper():
            return "_" + letter
    return None

upper_letter = find_upper(camel_case)

print(upper_letter)
