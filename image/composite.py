from PIL import Image,ImageDraw,ImageFilter  
size = (512,512)
im1 = Image.open('assets\\lena.jpg').resize(size)
im2 = Image.open('assets\\bridge.png').resize(size)

mask = Image.new("L",size,0)
draw = ImageDraw.Draw(mask)
draw.ellipse((100,100,(512-100),(512-100)),fill= 255)

mask.show()
im = Image.composite(im1,im2,mask)
im.show()