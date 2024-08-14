amount_due = 50
coins_permitted = [25, 10, 5]

#informar monto total
print("Amount due: " + str(amount_due))

#insertar moneda loop
while amount_due - coin_inserted > 0:
    coin_inserted = int(input("Insert coin: "))
    if coin_inserted in coins_permitted:
        amount_due = amount_due - coin_inserted
        print("Amount due: ", end="")
        print(amount_due)

#muestra el cambio en números positivos
else:
    print("Change Owed: ", end="")
    print(amount_due)

