import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    
    # search for a pattern
    if matches := re.findall(r'\bum\b', s, re.IGNORECASE):
        #print(matches)
        return len(matches)
    return 0


if __name__ == "__main__":
    main()