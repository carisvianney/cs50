time = input("What time is it? ")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) * 100.0 / 60.0
    hours = float(hours)
    global time
    time = hours + minutes

if 7.0 <= time < 9.0:
    print("breakfast time")
