from PIL import Image,ImageDraw,ImageFilter    

def crop_center(image,crop_width,crop_height):
    im_width,im_height = image.size
    return image.crop(((im_width-crop_width)//2,
                      (im_height-crop_height)//2,
                      (im_width+crop_width)//2,
                      (im_height+crop_height)//2))

def crop_max_square(image):
    return crop_center(image,min(image.size),min(image.size))

def expand2square(image,background_color):
    width,height = image.size  
    if width == height:
        return image  
    elif width>height:
        result = Image.new(image.mode,(width,width),background_color)
        result.paste(image,(0,(width-height)//2))
        return result
    elif height < width:
        result = Image.new(image.mode,(height,height),background_color)
        result.paste(image,((height-width)//2,0))
        return result 
    
def mask_circle_solid(image,background_color,blur_radius,offset=0):
    background = Image.new(image.mode,image.size,background_color)
    offset = blur_radius * 2 + offset 
    mask = Image.new('L',image.size,0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset,offset,(image.size[0]-offset),(image.size[1]-offset),),fill=255)
    mask= mask.filter(ImageFilter.GaussianBlur(blur_radius))
    return Image.composite(image,background,mask)
    
def mask_circle_transparent(image,blur_radius,offset=0):
    offset = blur_radius * 2 + offset 
    mask = Image.new('L',image.size,0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset,offset,(image.size[0]-offset),(image.size[1]-offset),),fill=255)
    mask= mask.filter(ImageFilter.GaussianBlur(blur_radius))
    
    result = image.copy()
    result.putalpha(mask)
    return result 