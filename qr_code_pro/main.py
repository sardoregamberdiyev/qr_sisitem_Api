import qrcode

payment_amount = 10.0
qr_data = f"payment:{payment_amount}"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(qr_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()
