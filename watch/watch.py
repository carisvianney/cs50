import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"^<iframe(?:.+)?(?:src\=\"http(?:s?)://(?:www\.)?youtube\.com/embed/(\w+)\")(?:.+)?$", s):
        return (f"https://youtu.be/{match.group(1)}")
    


if __name__ == "__main__":
    main()