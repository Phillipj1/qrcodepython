# qrcodepython
# Python QR Code Generator

This repository contains a simple Python script that generates a QR code using the `qrcode` library. This README provides step-by-step instructions on how to create a QR code with Python and save it as an image.

## Prerequisites

Before running the code, ensure you have the necessary libraries installed. You can install them using pip:

```bash
pip install qrcode[pil]

##Import the required libraries:

import qrcode
from PIL import Image

Create the QR code data by specifying the information you want to encode in the QR code. For example, a website URL:

data = "Name of the website.com"

#Generate the QR code:

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white")

Save the QR code as an image by specifying the desired file path:

image_path = "my_qr_code.png"
qr_img.save(image_path)
print(f"QR code saved as {image_path}")




