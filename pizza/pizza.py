from tabulate import tabulate
import csv
import sys

prices = []

def main():
    if len(sys.argv) == 1:
         sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
         sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        if not file_name.endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            try:
                with open(file_name) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        prices.append(row)
                    print(tabulate(prices, headers="keys", tablefmt="grid"))

            except FileNotFoundError:
                raise sys.exit(f"File does not exist")

main()