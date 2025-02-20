import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for group in match.groups():
            if int(group) > 255:
                return False
            else:
                pass
        return True
    return False


if __name__ == "__main__":
    main()