import qrcode
import pyzbar.pyzbar as pyzbar
# Set the data to encode
# data = '59-S1 59409'

# # Create the QR code instance
# qr = qrcode.QRCode(version=1, box_size=20, border=8)

# # Add the data to the QR code
# qr.add_data(data)

# # Make the QR code
# qr.make(fit=True)

# # Create an image from the QR code
# img = qr.make_image(fill_color="black", back_color="white")

# # Save the image
# img.save("qrcode.png")
def generate_qrcode(data):
    qr = qrcode.QRCode(version=1, box_size=15, border=8)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def scanqrcode(data):
    barcodes = pyzbar.decode(data)

    if barcodes:
        return barcodes[0].data.decode("utf-8")
    else:
        return None
