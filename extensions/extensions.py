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

if file_name.endswith(".pdf"):
    file_type = "pdf"
elif file_name.endswith(".zip"):
    file_type = "zip"

print("application/" + file_type)

if file_name.endswith(".txt"):
    file_type = "txt"
    print(file_type + "/plain")

else:
    
