from PIL import Image   

img = Image.open('assets\\color_tweak.png')

img = img.convert('RGBA')
R,G,B,Alpha = img.split()

img = Image.merge("RGBA",(G,R,B,Alpha))
img.show()