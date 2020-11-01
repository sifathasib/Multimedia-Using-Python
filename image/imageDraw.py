from PIL import Image,ImageDraw

txt = 'not really a fancy text'
size = (150,50)
color = (0,100,0)
img = Image.new('RGB',size,color)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((5,20),txt)
img.show()