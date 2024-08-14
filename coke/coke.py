
amount_due = 50
coins_permitted = [25, 10, 5]

print("Amount due: ", end="")
print(amount_due)

coin_inserted = int(input("Insert coin: "))

def main(amount_due):
    print("Amount due: ", end="")
    print(amount_due)

for coin in coins_permitted:
    if coin_inserted == coin:
        amount_due = amount_due - coin_inserted
        #print(amount_due)
        print("hello")

main(amount_due)
