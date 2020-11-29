import sys
from PyQt5.QtWidgets import QApplication,QDialog ,QInputDialog,QListWidgetItem
from demoListWidgetop import * 

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidget.addItem('chocolate')
        self.ui.listWidget.addItem('orange')
        self.ui.listWidget.addItem('green')
        self.ui.pushButtonAdd.clicked.connect(self.addList)
        self.ui.pushButtonEdit.clicked.connect(self.editList)
        self.ui.pushButtonDelete.clicked.connect(self.delItem)
        self.ui.pushButtonDeleteAll.clicked.connect(self.delallItem)
        self.show()
    def addList(self):
        text = self.ui.lineEditItem.text()
        if not text.isspace() and len(text)!=0:
            self.ui.listWidget.addItem(text)
        self.ui.lineEditItem.setText('') 
        self.ui.lineEditItem.setFocus()
    def editList(self):
         row = self.ui.listWidget.currentRow()
         newtext,ok = QInputDialog.getText(self,'Enter new text','enter new text')
         if ok and (len(newtext) != 0):
             self.ui.listWidget.takeItem(row)
             self.ui.listWidget.insertItem(row,QListWidgetItem(newtext))

    def delItem(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
    def delallItem(self):
        self.ui.listWidget.clear()
    
if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())