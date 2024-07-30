file_name = input("File name: ")
images = [".gif", ".png", ".jpg", ".jpeg"]
applications = []

if file_name.endswith(".gif"):
    file_name = "gif"
elif file_name.endswith(".png"):
    file_name = "png"
elif file_name.endswith(".jpg"):
    file_name = "jpg"
elif file_name.endswith(".jpeg"):
    file_name = "jpeg"

print("image/" + file_name)

if file_name.endswith(".txt"):
    file_name = "txt"
    print(file_name + "/plain")

elif file_name.endswith(".pdf"):
    file_name = "pdf"
elif file_name.endswith(".zip"):
    file_name = "zip"
else:
    file_name = "octet-stream"

print("application/" + file_name)
