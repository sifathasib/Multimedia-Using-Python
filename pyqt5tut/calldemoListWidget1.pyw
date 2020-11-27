import sys 
from PyQt5.QtWidgets import QApplication,QDialog  
from demoListWidget1 import * 

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidgetDiagnosisTest.itemSelectionChanged.connect(self.dispSelectedTest)
        self.show()
    def dispSelectedTest(self):
        self.ui.listWidgetSelectedTest.clear()
        items = self.ui.listWidgetDiagnosisTest.selectedItems()
        for i in list(items):
            self.ui.listWidgetSelectedTest.addItem(i.text())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
        