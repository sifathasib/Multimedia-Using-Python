from PIL import Image,ImageDraw,ImageFilter,ImageFont      

mask = Image.new('L',(512,512),0)
draw = ImageDraw.Draw(mask)
draw.ellipse((100,100,(512-100),(512-100)),fill=255)
mask.show()