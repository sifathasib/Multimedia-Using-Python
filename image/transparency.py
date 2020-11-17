from PIL import Image,ImageDraw,ImageFilter  

im1 = Image.open('assets\\lena.jpg')
im1.putalpha(200)

im1.show()