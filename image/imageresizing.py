from PIL import Image  

inpath = "D:\VS Code projects\Python Multimedia\\assets\sad.png"
img = Image.open(inpath)
width, height = 160,50
size = (width,height)
filterdict = {
    'Nearest': Image.NEAREST,
    'Bilinear': Image.BILINEAR,
    'Bicubic':Image.BICUBIC,
    "Antialias": Image.ANTIALIAS
}
for k in filterdict.keys(): 
    outpath = "D:\VS Code projects\Python Multimedia\\assets\\"+ k + ".png"
    filteropt = filterdict[k]
    #foo = img.resize(size,filteropt)
    img.thumbnail(size,filteropt)
    #foo.show()
    #foo.save(outpath)
    img.save(outpath)

