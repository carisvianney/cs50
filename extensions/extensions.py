file_name = lower(input("File name: "))
images = (".gif", ".png", ".jpg", ".jpeg")
applications = (".pdf", ".zip")

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

elif file_name.endswith(applications):
    if file_name.endswith(".pdf"):
        file_type = "pdf"
    else:
        file_type = "zip"

    print("application/" + file_type)

elif file_name.endswith(".txt"):
    print("text/plain")

else:
    print("application/octet-stream")
