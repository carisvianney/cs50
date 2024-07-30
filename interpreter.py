expression = input("Expression: ")
x, y, z = expression.split(" ")

x = int(x)

if y == "+":
    print(x + z)

elif y == "-":
    print(x - z)

elif y == "*":
    print(x * z)

elif y == "/":
    print(x / z)

