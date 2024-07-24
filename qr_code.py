# install/import libraries
# function that collects text and converts to qr code
# save qr code as image

import qrcode

def generate_qrcode(text, imageName):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="green", back_color="white")
    img.save(imageName + ".png")
    
url = input("\nEnter URL/Text: ")
saveAs = input("\nEnter file name: ")
generate_qrcode(url, saveAs)    

 