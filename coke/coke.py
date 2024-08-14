amount_due = 50
coins_permitted = [25, 10, 5]

#informar monto total
print("Amount due: " + str(amount_due))

#insertar moneda loop
while amount_due > 0:
    coin_inserted = int(input("Insert coin: "))
    amount_left = amount_due - coin_inserted
    print("Amount due: ", end="")
    print(amount_left)

"""
#restar moneda incluida en la lista al monto total
def main(amount_due):
    if coin_inserted in coins_permitted:
        amount_due = amount_due - coin_inserted
        print("Amount due: " + str(amount_due))

main(amount_due)
"""
