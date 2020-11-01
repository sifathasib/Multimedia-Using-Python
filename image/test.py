from PIL import Image
inputimage = Image.open("assets\sad.png")
inputimage.save("assets\sad1.png")
outputimage = Image.open("assets\sad1.png")
outputimage.show()