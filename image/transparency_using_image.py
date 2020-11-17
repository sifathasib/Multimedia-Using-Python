from PIL import Image,ImageDraw,ImageFilter  

im1 = Image.open('assets\\lena.jpg').resize((512,512))

#drawing alpha 
im_alpha = Image.new("L",(512,512),0)
draw = ImageDraw.Draw(im_alpha)
draw.ellipse((100,100,(512-100),(512-100)),fill= 255)

im_alpha = im_alpha.filter(ImageFilter.GaussianBlur(10))
im1.putalpha(im_alpha)

#im1 = im1.crop((100,100,(512-100),(512-100)))
im1.show()
#im_alpha.show()

