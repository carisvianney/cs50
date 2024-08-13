user_input = input("What time is it? ")

def main():
    # 8:30
    time = convert(user_input)
    # print(time)
    if 7.0 <= time < 8.0:
        print("breakfast time")
    elif 12.0 <= time < 13.0:
        print("lunch time")
    elif 18.0 <= time < 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60.0
    hours = float(hours) + minutes
    # print(hours, minutes)
    return hours

if __name__ == "__main__":
    main()
