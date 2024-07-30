file_name = input("File name: ")
images = [".gif", ".png", ".jpg", ".jpeg"]
applications = [".pdf", ".zip"]
text_app = "txt"

if file_name.endswith(".gif", ".png", ".jpg", ".jpeg"):
    print("image/" + file_name.endswith(3))

else:
    print("application/octet-stream")
