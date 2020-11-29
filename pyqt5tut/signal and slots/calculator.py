from demoCalculator import *  
import sys 
from PyQt5.QtWidgets import QApplication,QDialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonPlus.clicked.connect(self.addtwonum)
        self.ui.pushButtonSubtract.clicked.connect(self.subtracttwonum)
        self.ui.pushButtonMultiply.clicked.connect(self.multiplytwonum)
        self.ui.pushButtonDivide.clicked.connect(self.dividetwonum)
        self.show()
    def addtwonum(self):
        if len(self.ui.lineEditFirstNumber.text())!= 0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondNumber.text())!= 0:
            b= int(self.ui.lineEditSecondNumber.text())
        else: 
            b=0
        add = a+b 
        self.ui.labelResult.setText('addition '+str(add))
    def subtracttwonum(self):
        if len(self.ui.lineEditFirstNumber.text())!= 0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondNumber.text())!= 0:
            b= int(self.ui.lineEditSecondNumber.text())
        else: 
            b=0
        diff = a-b 
        self.ui.labelResult.setText('subtraction '+str(diff))
    def multiplytwonum(self):
        if len(self.ui.lineEditFirstNumber.text())!= 0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondNumber.text())!= 0:
            b= int(self.ui.lineEditSecondNumber.text())
        else: 
            b=0
        mult = a*b
        self.ui.labelResult.setText('multiplication '+str(mult))
    def dividetwonum(self):
        if len(self.ui.lineEditFirstNumber.text())!= 0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondNumber.text())!= 0:
            b= int(self.ui.lineEditSecondNumber.text())
        else: 
            b=0 
        div = a/b
        self.ui.labelResult.setText('dividened '+str(div))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
