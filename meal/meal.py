time = input("What time is it? ")

def main():
    

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) * 100.0 / 60.0
    hours = float(hours)
    time = hours + minutes

print(time)
