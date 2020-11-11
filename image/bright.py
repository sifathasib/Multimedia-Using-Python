from PIL import Image,ImageEnhance 

brightness = 5.0   
contrast = 1.3
peak = Image.open('assets\Before_brightened.png')
enhancer = ImageEnhance.Brightness(peak)
bright = enhancer.enhance(brightness)
bright.save('assets\\brightened.png')
bright.show()
#contrast
enhancer = ImageEnhance.Contrast(peak)
con = enhancer.enhance(contrast)
con.save('assets\\contrast.png')
con.show()
