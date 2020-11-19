from PIL import Image,ImageFilter  
import os 

paths = [
    'assets\\edge.png',
    'assets\\edge_enhance.png',
    'assets\\edge_detection.png',
    'assets\\edge_detection_2.png'
]

paths = map(os.path.normpath, paths)
(imgPath,outImagePath1,outImagePath2,outImagePath3)= paths 

img = Image.open(imgPath)
img1 = img.filter(ImageFilter.FIND_EDGES)
img1.save(outImagePath1)

img2 = img1.filter(ImageFilter.EDGE_ENHANCE)
img2.save(outImagePath2)

img3 = img2.filter(ImageFilter.FIND_EDGES)
img3 = img3.filter(ImageFilter.SMOOTH)
img3.save(outImagePath3)

img.show()
img1.show()
img2.show()
img3.show()