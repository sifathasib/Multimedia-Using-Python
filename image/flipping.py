from PIL import Image  

inpath = 'assets/flip.png'
outpath = 'assets/flip1.png'

img = Image.open(inpath)
foo = img.transpose(Image.FLIP_LEFT_RIGHT)
foo.save(outpath)
foo.show()