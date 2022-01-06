import qrcode
img = qrcode.make("https://www.linkedin.com/in/be-thanymarshall/")
img.save("LinkedIn.jpg")