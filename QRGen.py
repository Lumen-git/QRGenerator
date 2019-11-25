
import qrcode

# QR settings
qr = qrcode.QRCode(
    version = 15,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 20,
    border = 4,
)

# The text to QRify
data = str(input("TXT: "))

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
img.save("image.jpg")
