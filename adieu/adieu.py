import sys
import inflect

p = inflect.engine()

names = []

def main():
    
    # Ask for a name until users input Ctrl + d
    while True:
        try:
            names.append(input("Name: "))
            name_list = p.join(names)
            
        except EOFError:

            print(" ")
            print("Adieu, adieu, to " + str(name_list))
            sys.exit()            

            # Print Adieu, adieu, to "name" if it is only one name given... print Adieu, adieu, to "name" and "name" if theres more than one name

main()