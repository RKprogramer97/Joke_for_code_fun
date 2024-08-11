import qrcode
qr_image = qrcode.make("Hi ever")
qr_image.save("qr_image.jpg")
