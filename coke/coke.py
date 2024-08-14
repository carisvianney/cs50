amount_due = 50
coins_permitted = [25, 10, 5]

print("Amount due:", end="")
print(amount_due)

coin_inserted = int(input("Insert coin: "))

def insert_coin(coin_inserted):
    while coin_inserted in coins_permitted:
        amount_due = amount_due - coin_inserted
        print("Amount due:", end="")
        print(amount_due)


