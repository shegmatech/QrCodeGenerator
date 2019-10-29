import os
import pyqrcode
import png #pyqrcode cant generate png images so i need to use this module to generate png.

# getting document path with os
path = 'C:\\Users\\MSE\\PycharmProjects\\qrcode_gen\\Passport' #change this path to where your passports are located

# using os to get the file name without extention
files = [os.path.splitext(filename)[0] for filename in os.listdir(path)]
print(files)
# iterating through files and printing the filename in an array
for line in files:
    i = str(line)
    #using pyqrcode to create the barcode
    qr = pyqrcode.create(line)
    #Barcode output with the filename
    qr.png(line + '.png', scale=5)
    qr.png(line + '.png', scale=5, )

