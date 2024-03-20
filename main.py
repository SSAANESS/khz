import qrcode

data = 'Gravestone'
qr = qrcode.QRCode(version=5, box_size=15, border=10)
qr.add_data(data)

img = qr.make_image()

img.save('qrcode.png')
