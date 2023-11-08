import qrcode
from PIL import Image
##QR code "https://www.skytre3d.com/"

data = "Website name"

qr = qrcode.QRCode(
    version=1,     # specifies the QR code version (1 to 40).
    error_correction=qrcode.constants.ERROR_CORRECT_L,  ## sets the error correction level (you can choose 
    box_size=10,  #determines the size of each QR code "box."
    border=4, #specifies the border size around the QR code.
)
qr.add_data(data) #adds the data to the QR code.
qr.make(fit=True) #generates the QR code.

qr_img = qr.make_image(fill_color="black", back_color="white")


qr_img.save("my_qr_code.png")  # Save the QR code as an image
qr_img.show()  # Display the QR code
