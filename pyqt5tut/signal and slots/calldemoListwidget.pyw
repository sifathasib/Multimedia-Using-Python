import sys 
from demoListWidget import * 
from PyQt5.QtWidgets import QApplication,QDialog

class Myform(QDialog):
    def __init__(self):
        
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.listWidgetDiagnosis.itemClicked.connect(self.dispSelected)
        self.show()
        
    def dispSelected(self):
        self.ui.labeltest.setText("selected test: "+ self.ui.listWidgetDiagnosis.currentItem().text()) 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w= Myform()
    w.show()
    sys.exit(app.exec_())