time = input("What time is it? ")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) * 100.0 / 60.0
    hours = float(hours)

if 7 <= hours < 9:
    print("breakfast time")
