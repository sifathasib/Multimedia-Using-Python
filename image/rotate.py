from PIL import Image  

inpath = "assets\\test.jpg"
outpath = 'assets\\test1.jpg'

img = Image.open(inpath)
deg = 45
filteropt = Image.BILINEAR
#foo = img.rotate(deg,filteropt)
foo = img.transpose(Image.ROTATE_270)
foo.save(outpath)
foo.show()