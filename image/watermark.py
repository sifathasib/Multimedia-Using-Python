from PIL import Image,ImageDraw,ImageFont 
import os,getopt,sys 
from datetime import date

class watermark:
    
    def __init__(self):
        #image path 
        self.mainImagePath = ''
        self.waterMarkPath = ''
        #text to be embeded  
        self.text = ''
        #transparency factor 
        self.factor = 0.5   
        # anchor point for embeded text 
        self.text_pos =(0,0)
        #anchor point for watermark    
        self.mark_pos = None  
        # Date stamp   
        self.dateStamp = False  
        #   Image objects
        self.mainImage = None 
        self.waterMark = None 
        self.processArgs()
        self.createImageObj()
        self.addText()
        self.addWaterMark()
        
        if self.dateStamp:
            self.addDateStamp()
            self.mainImage.save('assets\\watermark.png')
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
        year,month,day = time_tpl[0] ,time_tpl[1],time_tpl[2]
        datestamp = str(year)+"/"+str(month)+"/"+str(day)
        self._addTextWorker(datestamp,dateStamp=True)  
    def _addTextWorker(self,txt,dateStamp=False):
        size = self.mainImage.size
        color = (0,0,0)
        textFont= ImageFont.truetype('arial.ttf',50)
        imgDrawer = ImageDraw.Draw(self.mainImage)   
        textSize = imgDrawer.textsize(txt,textFont)
        if dateStamp:
            pos_x = min(2,size[0])
            pos_y = size[1]-texxtSize[1]
            pos =(pos_x,pos_y)
        else:
            pos= self.text_pos    
        imgDrawer.text(pos,txt,font=textFont)
        if(textSize[0]>size[0] or textSize[1]>size[1]):
            print('text going out of bounds')
        
    def addWaterMark(self):
        using_composite =False   
        if self.watermark is None:
            return  
        self.watermark = self.addTransparency(self.watermark)
        pos_x, pos_y = self._getMarkPosition(self.mainImage,self.watermark)  
        if not_using_composite:
            self.mainImage.paste(self.watermark,(pos_x,pos_y),self.watermark)
        else: 
            
    def addTransparency(self,img):
        pass 
    def createImageObj(self):
        pass  
    def _getMarkPosition(self,canvasImage,markImage):
        pass  
    def processArgs(self):
        args = sys.argv[1:]
        shortopts = ''
        longopts = ['image1=','watermark=','markpos=','text=',
                    'text_pos=','transparency=','dateStamp=']
        try:
            opts,args = getopt.getopt(args,shortopts,longopts)
        except getopt.GetoptError,error:
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
            elif opt== '--watermark':
                assert os.path.exist(val)
                self.waterMarkPath = val
            elif opt ==  '--markpos': 
                val = val.split(',')
                assert len(val)==2 
                self.mark_pos =(int(val[0]),int(val[1]))
            elif opt == '--text': 
                assert val  
                self.text = val 
            elif opt == '--transparency':
                self.factor = float(val)
            elif opt == '--text_pos':
                val = val.split(',')
                assert len(val)== 2
                self.text_pos =(int(val[0]),int(val[1]))
            elif opt == '--dateStamp':
                self.dateStamp = bool(val)
                print('***dateStamp',self.dateStamp)
        if not self.mainImagePath:
            self.printUsage()
            sys.exit(2)
            
    def printUsage(self):
        pass   
    