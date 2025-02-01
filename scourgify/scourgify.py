import sys
import csv

name_list = []

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # quites este else 
    else:
        try:
            with open(sys.argv[1]) as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    name_list.append(row)
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
        
        with open(sys.argv[2], "w", newline="") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in name_list:
                last, first = row["name"].split(", ")
                new_row = {
                    "first": first,
                    "last": last,
                    "house": row["house"]
                }
                writer.writerow(new_row)
            

main()