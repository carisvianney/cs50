user_input = input("What time is it? ")

def main():
    # 8:30
    time = convert(user_input)
    # print(time)
    if time >= 7.0 and time < 8.0:
        print("breakfast time")
    elif time >= 12.0 and time < 13.0:
        print("lunch time")
    elif time >= 18.0 and time < 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60.0
    hours = float(hours) + minutes
    # print(hours, minutes)
    time = hours
    return time

if __name__ == "__main__":
    main()
