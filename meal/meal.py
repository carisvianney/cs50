time = input("What time is it? ")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) * 100.0 / 60.0
    hours = float(hours) + minutes
    time = hours

def main():
    # 8:30
    convert(time)
    print(time)
    if 7.0 <= time < 9.0:
        print("breakfast time")
    elif 12.0 <= time < 13.0:
        print("lunch time")
    elif 18.0 <= time < 19.0:
        print("dinner time")

main()
