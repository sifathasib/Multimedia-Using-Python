from demoFontCombobox import *
import sys 
from PyQt5.QtWidgets import QApplication,QDialog 

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        myfont = QtGui.QFont(self.ui.fontComboBox.itemText(self.ui.fontComboBox.currentIndex()),15)
        self.ui.textEdit.setFont(myfont)
        self.ui.fontComboBox.currentFontChanged.connect(self.changeFont)
        self.show()
        
    def changeFont(self):
        myfont = QtGui.QFont(self.ui.fontComboBox.itemText(self.ui.fontComboBox.currentIndex()),15)
        self.ui.textEdit.setFont(myfont)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())