from pyfiglet import Figlet
figlet = Figlet()

figlet.getFonts()

import random
import sys

# define 0 or two valid text args:
if len(sys.argv) == 1 or len(sys.argv) == 3:
        
    # expect 0 args to give random font
    if len(sys.argv) == 1:

        Input = input("Input: ")
        figlet.setFont(font=random.choice(figlet.getFonts()))
        print(figlet.renderText(Input))

    # expect 2 args to define the font, first one has to be -f or --font
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in figlet.getFonts():
                
                Input = input("Input: ")
                
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(Input))
            
            else:
                print("Invalid usage")
                sys.exit(1)

        else:
                print("Invalid usage")
                sys.exit(1)

    # exit sys and print Invalid usage
else:
    print("Invalid usage")
    sys.exit(1)