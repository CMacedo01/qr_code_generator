import qrcode
import image

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = input("Enter a URL to convert into a QR Code: ")
#Sample URL: https://www.nba.com/

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color="white")
img.save("QR_Code.png")

#Image will generate in file titled QR_Code.png