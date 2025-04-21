import qrcode
data='https://github.com/Lalith-47/Python'
qr=qrcode.make(data)
qr.save('QrCode.jpeg')
print('qrCode generated successfully')
