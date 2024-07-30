Greeting = str.lower(input("Greeting: "))

if "hello" in Greeting:
    print("$0")

elif Greeting.startswith("h"):
    print("$20")

else:
    print("$100")
