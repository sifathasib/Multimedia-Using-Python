from PIL import Image,ImageDraw,ImageFilter 
from thumbnail import *  
import os,glob   

src_dir = "assets\\"
dst_dir = 'assets\\thumbnails\\'
files = glob.glob(os.path.join(src_dir,'*.png'))


for f in files:
    im = Image.open(f)
    im_square = crop_max_square(im)
    im_thumb = mask_circle_transparent(im_square,4)
    ftitle,ftext = os.path.splitext(os.path.basename(f))
    im_thumb.save(os.path.join(dst_dir,ftitle+'_thumbnail'+ftext),quality=95)
