file_name = input("File name: ")
images = [".gif", ".png", ".jpg", ".jpeg"]
applications = [".pdf", ".zip"]
text_app = "txt"

if file_name.endswith(".gif")or(".png")or(".jpg")or(".jpeg"):
    print("image/" + file_name)

else:
    print("application/octet-stream")
