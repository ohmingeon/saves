import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import uppercasebase
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic import *

aui = uic.loadUiType("aui.ui")[0]

class AnswerWindow(QMainWindow, aui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pi.setPixmap(QtGui.QPixmap("1624199764.webp"))
        self.setFixedSize(900, 500)


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    widget = QtWidgets.QStackedLayout()
 
    AnswerWindow = AnswerWindow()

    widget.addWidget(AnswerWindow)

    #프로그램 화면을 보여주는 코드
    AnswerWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()