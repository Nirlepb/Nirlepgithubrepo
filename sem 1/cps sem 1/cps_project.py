import qrcode
import os  # [1] Import os to handle folder creation

# Accepted the user input
print("Enter the website you need to make QR Code")
s = input()

# QR code box structure
q = qrcode.QRCode(version=1, box_size=10, border=5)

# adding data and fit it.
q.add_data(s)
q.make(fit=True)

# importing as a image
img = q.make_image(fill="black", back_color="white")

# [2] Check if 'static' folder exists, if not, create it
if not os.path.exists("static"):
    os.makedirs("static")

# [3] Save using forward slash to avoid SyntaxWarning
img.save("nirlepqrcode.jpg")

print("QR code saved successfully in nirlepqrcode.jpg!")