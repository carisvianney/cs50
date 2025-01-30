import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        if not file_name.endswith(".py"):
            sys.exit("Not a Python file")
        else:
            try:
                with open(file_name) as file:
                    lines = 0
                    for line in file:
                        line = line.lstrip()
                        if line.strip():
                            if not line.startswith("#"):
                                lines = lines + 1
                    print(lines)
                            
            except: 
                FileNotFoundError("File does not exist")
main()