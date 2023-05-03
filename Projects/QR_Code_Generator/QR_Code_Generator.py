import pyqrcode

# To take input the data for the QR Code
data = input("Enter the Link or Text to generate QR Code :- ")

# To create the QR Code form the given input data
qr = pyqrcode.create(data)

# To save the QR Code created for the data un svg format
qr.svg('qr_code.svg', scale=8)
