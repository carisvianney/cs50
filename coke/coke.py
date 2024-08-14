coke = 50
coins_permitted = [25, 10, 5]
print("Amount due: " + str(coke))

coin_inserted = int(input("Insert coin: "))

if coin_inserted in coins_permitted:
    amount_due = coke - coin_inserted
