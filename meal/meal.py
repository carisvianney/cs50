time = input("What time is it? ")

def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) * 100

if 7 <= hours < 9:
    print("breakfast time")
