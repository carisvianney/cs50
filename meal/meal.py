time = input("What time is it? ")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) * 100.0 / 60.0

main()

print(time)
