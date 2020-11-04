import sys
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("grid layout")

layout = QGridLayout()
layout.addWidget(QPushButton('button1'),0,0)
layout.addWidget(QPushButton('button2'),0,1)
layout.addWidget(QPushButton('button3'),0,2)
layout.addWidget(QPushButton('button4'),1,0,1,3)
#layout.addWidget(QPushButton('button5'),1,1)
#layout.addWidget(QPushButton('button6'),1,2)
layout.addWidget(QPushButton('button7'),2,0)
layout.addWidget(QPushButton('button8'),2,1,1,2)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())