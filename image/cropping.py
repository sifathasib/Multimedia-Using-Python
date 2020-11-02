from PIL import Image  
img = Image.open("assets\\test.jpg")
left,upper,right,lower = 0,0,400,400

bbox = (left,upper,right,lower)
img = img.crop(bbox)
img.save("assets\\test1.jpg")
img.show()