amount_due = 50
coins_permitted = [25, 10, 5]

#informar monto total
print("Amount due: " + str(amount_due))

#insertar moneda
coin_inserted = int(input("Insert coin: "))

#restar moneda incluida en la lista al monto total
if coin_inserted in coins_permitted:
    amount_due = amount_due - coin_inserted
    print("Amount due: " + str(amount_due))
