
amount_due = 50
coins_permitted = [25, 10, 5]

def main(amount_due):
    print("Amount due:", end="")
    print(amount_due)

coin_inserted = int(input("Insert coin: "))

for coin in coins_permitted:
    if coin_inserted == coin:
        amount_due = amount_due - coin_inserted
        print(amount_due)

main(amount_due)
