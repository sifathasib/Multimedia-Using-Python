import sys 
from demoSlider import * 
from PyQt5.QtWidgets import QApplication,QDialog 

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.horizontalScrollBarSugerlevel.valueChanged.connect(self.scrollhorizontal)
        self.ui.horizontalSliderbloodPressure.valueChanged.connect(self.slidehorizontal)
        self.ui.verticalScrollBarPulseRate.valueChanged.connect(self.scrollvertical)
        self.ui.verticalSliderCholestorol.valueChanged.connect(self.slidevertical)
        self.show()
        
    def scrollhorizontal(self,value):
        self.ui.lineEditResult.setText('suger level : '+str(value))
    def slidehorizontal(self,value):
        self.ui.lineEditResult.setText('blodd pressure : '+str(value))  
    def scrollvertical(self,value):
        self.ui.lineEditResult.setText('Pulse Rate : '+str(value))
        
    def slidevertical(self,value):
        self.ui.lineEditResult.setText('cholestorol : '+str(value)) 
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())