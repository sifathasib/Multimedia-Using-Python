import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('vbox layout')
window.setGeometry(100,100,200,200)
layout = QVBoxLayout()
layout.addWidget(QPushButton('top'))
layout.addWidget(QPushButton('middle'))
layout.addWidget(QPushButton('bottom'))
window.setLayout(layout)
window.show()

sys.exit(app.exec_())