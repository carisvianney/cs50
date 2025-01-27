def main():
    Greeting = str.lower(input("Greeting: "))
    print(f"${value(Greeting)}")


def value(greeting):
    if "hello" in greeting:
        return 0

    elif greeting.startswith("h"):
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()
