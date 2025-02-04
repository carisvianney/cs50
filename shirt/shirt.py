import sys
import os.path
from PIL import Image, ImageOps
import requests

# Validación de command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

valid_ends = [".jpg", ".jpeg", ".png"]
file_1 = sys.argv[1]
file_2 = sys.argv[2]

name1, ext1 = os.path.splitext(file_1) 
name2, ext2 = os.path.splitext(file_2) 

if not ext1 in valid_ends and not ext2 in valid_ends:
    sys.exit("Invalid input")
elif not ext1 == ext2:
    sys.exit("Input and output have different extensions")


# Lectura del input y superposición del png
with Image.open(file_1) as photo:
    shirt = Image.open("shirt.png")
    size = shirt.size
    print(size)
    
    photo = ImageOps.fit(photo, size=size)
    photo.paste(shirt, shirt)
    photo.save(file_2)
