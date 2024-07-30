file_name = input("File name: ")

if file_name.endswith(".gif"):
    file_type = "gif"
elif file_name.endswith(".png"):
    file_type = "png"
elif file_name.endswith(".jpg"):
    file_type = "jpg"
elif file_name.endswith(".jpeg"):
    file_type = "jpeg"

print("image/" + file_type)

.txt
.zip
.pdf
