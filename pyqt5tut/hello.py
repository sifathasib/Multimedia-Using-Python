import sys  
from PyQt5.QtWidgets import QApplication,QLabel,QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('pyqt5')
window.setGeometry(100,100,280,80)
window.move(60,15)
hellomsg = QLabel('<h1> hello world</h1>',parent=window)
hellomsg.move(60,15)

window.show()
sys.exit(app.exec_())
