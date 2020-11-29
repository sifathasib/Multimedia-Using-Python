import sys 
from demoCombobox import *
from PyQt5.QtWidgets import QApplication,QDialog  

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBoxAccountType.currentIndexChanged.connect(self.dispAccountType)
        self.show()
    def dispAccountType(self):
        self.ui.labelAccountType.setText('you have selected: '+ self.ui.comboBoxAccountType.itemText(self.ui.comboBoxAccountType.currentIndex()))
if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())