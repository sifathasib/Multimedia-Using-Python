from PIL import Image

img = Image.open('assets\\color_tweak.png')
r,g,b,alpha = img.split()
selection = r.point(lambda x:x>150 and 0)
selection.save('assets\color_band_mask.png')
r.paste(g,None,selection)
#selection.show()
img = Image.merge("RGBA",(r,g,b,alpha))
img.show()
#g.show()
