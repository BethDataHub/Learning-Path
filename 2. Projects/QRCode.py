import qrcode
from PIL import Image

link=input("Input the link to use for the qr code: ")
img = qrcode.make(link)
img.save("LinkedIn.jpg")

img = Image.open('LinkedIn.jpg')
img.show() 