from PIL import Image,ImageDraw,ImageFilter 

im1 = Image.open('assets\\bridge.png').resize((512,512))
im2 = Image.open('assets\\lena.jpg').resize((512,512))

mask = Image.open('assets\\horse.png').convert('L').resize((512,512))
mask.show()
im = Image.composite(im2,im1,mask)
im.show()