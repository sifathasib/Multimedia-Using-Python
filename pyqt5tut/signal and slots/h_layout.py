import sys
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QApplication,QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QhboxLayout')

layout = QHBoxLayout()
layout.addWidget(QPushButton('left'))
layout.addWidget(QPushButton('center'))
layout.addWidget(QPushButton('right'))

window.setLayout(layout)
window.show()
sys.exit(app.exec_())

