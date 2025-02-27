import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.search(r"^(\d(?:\d)?(?:\:\d{2})?)\ (AM|PM)( .* )(\d(?:\d)?(?:\:\d{2})?)\ (AM|PM)$", s):
        
        # groups into hours
        if ":" in match.group(1):
            hours1, minutes1 = match.group(1).split(":")
            hours1 = int(hours1)
            minutes1 = int(minutes1)
        else:
            hours1 = int(match.group(1))
            minutes1 = 00

        if ":" in match.group(4):
            hours2, minutes2 = match.group(4).split(":")
            hours2 = int(hours2)
            minutes2 = int(minutes2)
        else:
            hours2 = int(match.group(4))
            minutes2 = 00
        

        # raise ValueError
        if minutes1 > 59 or minutes2 > 59:
            raise ValueError("Too many minutes")
        elif not " to " in match.group(3):
            raise ValueError(" to  omitted")
        elif "-" in match.group(3):
            raise ValueError("Unknown symbol")
        elif hours1 > 12 or hours2 > 12:
            raise ValueError("Out-of-range hours")
        

        # convert to 24 hours
        if match.group(2) == "PM":
            if hours1 < 12:
                hours1 = hours1 +12
        else:
            if hours1 == 12:
                hours1 = hours1 -12

        if match.group(5) == "PM":
            if hours2 < 12:
                hours2 = hours2 +12
        else:
            if hours2 == 12:
                hours2 = hours2 -12


        return (f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}")
    raise ValueError("No match found by re.search")
               

if __name__ == "__main__":
    main()