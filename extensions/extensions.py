file_name = input("File name: ")
images = (".gif", ".png", ".jpg", ".jpeg")
applications = [".pdf", ".zip"]
text_app = "txt"

if file_name.endswith(images):
    if file_name.endswith(".gif"):
        file_type = "gif"
    elif file_name.endswith(".png"):
        file_type = "png"
    elif file_name.endswith(".jpg"):
        file_type = "jpg"
    else:
        file_type = "jpeg"

    print("image/" + file_type)

else:
    print("application/octet-stream")
