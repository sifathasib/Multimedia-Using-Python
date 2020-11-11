from PIL import Image

img1 = Image.open('assets\\bridge.png')
img1 = img1.convert('RGBA')

img2 = Image.open('assets\\birds.png')
img2 = img2.convert('RGBA')

img = Image.blend(img1,img2,0.3)
img= img.convert('L')
img.show()
