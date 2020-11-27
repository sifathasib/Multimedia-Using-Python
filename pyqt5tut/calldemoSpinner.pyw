import sys 
from demoSpinner import * 
from PyQt5.QtWidgets import QDialog,QApplication 

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.spinBoxBookQty.editingFinished.connect(self.result1)
        self.ui.doubleSpinBoxSugarQty.editingFinished.connect(self.result2)
        self.show()
        
    def result1(self):
        if len(self.ui.lineEditBookPrice.text()) != 0:
            bookPrice = int(self.ui.lineEditBookPrice.text())
        else:
            bookPrice = 0 
        totalBookamount = self.ui.spinBoxBookQty.value() * bookPrice
        self.ui.lineEditBookAmount.setText(str(totalBookamount))
        
    def result2(self):
        if len(self.ui.lineEditSugarPrice.text())!=0:
            sugarPrice = int(self.ui.lineEditSugarPrice.text())
        else: 
            sugarPrice = 0 
        totalSugaramount = self.ui.doubleSpinBoxSugarQty.value() * sugarPrice
        self.ui.lineEditSugarAmount.setText(str(totalSugaramount))
        bookamount = int (self.ui.lineEditBookAmount.text())
        totalamount = bookamount + totalSugaramount
        self.ui.label_3.setText(str(totalamount))♠
if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())