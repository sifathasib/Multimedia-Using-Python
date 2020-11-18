from PIL import Image,ImageDraw,ImageFont  
import os,sys,getopt 
from datetime import date 

class waterMark():
    
    def __init__(self):
        
        self.waterMarkPath = ''
        self.mainImagePath = ''
        self.text = ''
        self.t_factor = 0.5
        self.text_pos = (0,0)
        self.mark_pos = None 
        self.dateStamp = False 
        self.waterMark = None 
        self.mainImage = None  
        
        self.processArgs()
        self.createImageObjects()
        self.addText()
        self.addWaterMark()
        
        if self.dateStamp:
            self.addDateStamp()
            self.mainImage.save('assets\\wm.png')
            self.mainImage.show()
          
    def addText(self):
        if not self.text:
            return  
        if self.mainImage is None:
            print('main image is not defined')
            return  
        txt = self.text 
        self._addTextWorker(txt)
        
          
    def addDateStamp(self):
        today = date.today()
        time_tpl = today.timetuple()
        year,month,day = time_tpl[0],time_tpl[1],time_tpl[2]
        dateStamp = str(year)+"/"+str(month)+"/"+str(day)
        self._addTextWorker(dateStamp,dateStamp=True)
          
    def _addTextWorker(self,txt,dateStamp = False):
        size = self.mainImage.size
        color = (0,0,0)
        textFont = ImageFont.truetype('arial.ttf',50)
        imgDrawer = ImageDraw.Draw(self.mainImage) 
        textSize = imgDrawer.textsize(txt,textFont)
        if dateStamp:
            pos_x = min(2,size[0])
            pos_y = size[1] - textSize[1]
            pos = (pos_x,pos_y)
        else:
            pos = self.text_pos  
        imgDrawer.text(pos,txt,font= textFont)
        if (textSize[0]>size[0] or textSize[1]>size[1]):
            print('text going out of bounds')  
            
                     
    def addWaterMark(self):
        using_composite = False 
        if self.waterMark is None:
            return 
        self.waterMark = self.addTransparency(self.waterMark)
        pos_x,pos_y = self._getMarkPosition(self.mainImage,self.waterMark)
        if not using_composite:
            self.mainImage.paste(self.waterMark,(pos_x,pos_y),self.waterMark)
        else:
            canvas = Image.new('RGBA',self.mainImage.size,(0,0,0,0))
            canvas.paste(self.waterMark,(pos_x,pos_y))
            self.mainImage = Image.composite(canvas,self.mainImage,canvas) 
            
    def addTransparency(self,img):
        img = img.convert('RGBA')
        img_blender = Image.new("RGBA",img.size,(0,0,0,0))
        img = Image.blend(img_blender,img,self.t_factor)
        return img    
          
          
    def createImageObjects(self):
        self.mainImagePath = os.path.normpath(self.mainImagePath)
        self.mainImage = Image.open(self.mainImagePath) 
        if self.waterMarkPath:
            self.waterMarkPath = os.path.normpath(self.waterMarkPath)
            self.waterMark = Image.open(self.waterMarkPath)
            
    def _getMarkPosition(self,canvasImage,markImage):
        if self.mark_pos is not None:
            return self.mark_pos
        canvas_width,canvas_height = canvasImage.size
        mark_width,mark_height = markImage.size
        pos_x = canvas_width- mark_width
        pos_y = canvas_height- mark_height
        return (pos_x,pos_y)
    
    def processArgs(self):
        args = sys.argv[1:]
        shortopts = ''
        longopts =['image1=','watermark=','mark_pos=',
                   'text=','text_pos=','transparency=',
                   'dateStamp=']
        try:
            opts,args = getopt.getopt(args,shortopts,longopts)
        except getopt.GetoptError:
            self.printUsage()
            sys.exit(error)
        if not len(opts):
            self.printUsage()
            sys.exit(2)
        for opt,val in opts:
            print(opt)
            if opt == '--image1': 
                assert os.path.exists(val)
                self.mainImagePath = val 
            elif opt == '--watermark': 
                assert os.path.exists(val)
                self.waterMarkPath = val
            elif opt == '--text': 
                assert val 
                self.text = val 
            elif opt == '--mark_pos': 
                val = val.split(",")
                assert len(val) == 2
                self.mark_pos = (int(val[0]),int(val[1]))
            elif opt == '--text_pos':
                val = val.split(",")
                assert len(val)==2
                self.text_pos = (int(val[0]),int(val[1]))
            elif opt == '--transparency': 
                self.t_factor = float(val)
            elif opt == '--dateStamp':
                self.dateStamp = bool(val)
                print('***dateStamp',self.dateStamp)
        if not self.mainImagePath:
            self.printUsage()
            sys.exit(2)
        
         
    def printUsage(self):
        print('hello this is watermark') 
    
waterMark()