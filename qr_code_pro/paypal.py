import paypalrestsdk
import qrcode

paypalrestsdk.configure({
    "mode": "sandbox",  # or "live"
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
})

payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"
    }
})

transaction = paypalrestsdk.Transaction({
    "amount": {
        "total": "10.00",
        "currency": "USD"
    },
    "description": "Withdrawal through QR code payment"
})

payment.transactions.append(transaction)

qr_request = paypalrestsdk.QrCodeRequest({
    "merchant_info": {
        "email": "YOUR_PAYPAL_EMAIL",
        "first_name": "John",
        "last_name": "Doe"
    },
    "amount": {
        "currency": "USD",
        "total": "10.00"
    },
    "invoice_number": "12345",
    "item_list": {
        "items": [{
            "name": "Withdrawal",
            "quantity": 1,
            "price": "10.00",
            "currency": "USD"
        }]
    }
})

# pay qismi yani qr qismi
qr_data = f"payment:{qr_request}"

qr = qrcode.QRCode(version=1, box_size=40, border=20)
qr.add_data(qr_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

qr_code = qr_request.create()
qr_url = qr_code.open(img)

payment_id = payment["id"]
payment = paypalrestsdk.Payment.find(payment_id)
status = payment["state"]
