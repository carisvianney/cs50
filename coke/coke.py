
amount_due = 50
coins_permitted = [25, 10, 5]

print("Amount due:", end="")
print(amount_due)

coin_inserted = int(input("Insert coin: "))

def main(amount_due):
    while True:
        for coin_inserted in coins_permitted:
            amount_due = amount_due - coin_inserted
        print("Amount due:", end="")
        print(amount_due)
        coin_inserted = int(input("Insert coin: "))

for coin in coins_permitted:
    if coin_inserted == coin:
        amount_due = amount_due - coin_inserted


"""
def insert_coin(coin_inserted):
    while coin_inserted in coins_permitted:
        amount_due = 50 - coin_inserted
        print("Amount due:", end="")
        print(amount_due)
        break

for coin_inserted
insert_coin(coin_inserted)
"""


main(amount_due)
