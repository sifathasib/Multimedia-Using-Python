from PIL import Image
img1 = Image.open("assets\\sad.png")      
img2 = Image.open("assets\\test.jpg")
left,upper,right,lower = 0,25,180,210
bbox_1 = (left,upper,right,lower)
crp = img1.crop(bbox_1)
crp = crp.transpose(Image.FLIP_TOP_BOTTOM)
bbox_2 = (0,210)
img2.paste(crp,bbox_2)
img2.save("assets\\paste.jpg")
img2.show()