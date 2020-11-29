import sys 
from PyQt5.QtWidgets import QDialog,QApplication 

from demoCheckBox1 import * 

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxCheese.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxOlive.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSausege.stateChanged.connect(self.dispAmount)
        self.show()
    def dispAmount(self):
        amount = 10 
        if self.ui.checkBoxCheese.isChecked() == True:
            amount = amount +1 
        if self.ui.checkBoxOlive.isChecked() == True:
            amount = amount+2 
        if self.ui.checkBoxSausege.isChecked()==True:
            amount = amount +1
        self.ui.labelAmount.setText('total prize for pizza is : '+ str(amount))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())