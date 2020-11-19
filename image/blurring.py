from PIL import Image,ImageFilter  

img = Image.open('assets\\blur.png')
img = img.filter(ImageFilter.BLUR)
img.show()