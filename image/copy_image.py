from PIL import Image   
from PIL import ImageDraw,ImageFilter  

im1 = Image.open('assets\\bridge.png')
im2 = Image.open('assets\\foo.png')
#mask image 
mask_im = Image.new('L',im2.size,0)
draw = ImageDraw.Draw(mask_im)
w, h = im2.size
draw.ellipse([(5,5),(w-5,h-5)],fill=255,outline = 'red')
#mask_im.show()
cpy = im1.copy()
box =(100,100)
cpy.paste(im2,box,mask_im)
cpy.show()
