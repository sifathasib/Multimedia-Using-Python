from PIL import Image,ImageDraw

txt = 'FLIP'
outpath = 'assets/flip.png'
size = (80,80)
color = (0,100,0)
img = Image.new('RGB',size,color)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((30,30),txt)
img.show()
img.save(outpath)