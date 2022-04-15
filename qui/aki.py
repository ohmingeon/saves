import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import uppercasebase
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic import *
import pandas as pd
import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
qui = uic.loadUiType("qui.ui")[0]
aui = uic.loadUiType("aui.ui")[0]
data = pd.read_csv("학교 교직원 정보.csv", header=0)
QT = pd.read_csv("질문.csv")
count = 0
an=0
kk=0
qch=0
class Question:
    def rd(self, qname, qabout, qanswer):
        self.qname = qname
        self.qabout = qabout
        self.qanswer = qanswer
        print('질문은 {0}이고 찾는 건 {1}이며 대답은 {2}입니다.'.format(self.qname,self.qabout,self.qanswer))
        if self.qanswer == 3:
            data1 = data[data[QT.iloc[0,self.qname]] == self.qabout].index
            data.drop(data1,inplace=True)
        elif self.qanswer == 1:
            data1 = data[data[QT.iloc[0,self.qname]] != self.qabout].index
            data.drop(data1,inplace=True)
        global an
        an=0
        print(data.성명)

Que = Question()

#화면을 띄우는데 사용되는 Class 선언
class MainWindow(QMainWindow, qui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(900, 500)
        self.pushButton.clicked.connect(self.button1Function)
        self.pushButton_2.clicked.connect(self.button2Function)
        self.pushButton_3.clicked.connect(self.button3Function)
        global count, qn, qch, rn, kk
        count=1
        qch+=1
        qn = QT.iloc[1,count]
        rn = random.randint(1, 15)
        kk = QT.iloc[rn+1,count]
        self.Q.setText(kk + qn)
        


    def button1Function(self) :
        global count, an, kk ,qch
        if qch>=7 or len(data.성명) <=1 :
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            an = 1
            Que.rd(count,kk,an)
            count+=1
            qch+=1
            qn = QT.iloc[1,count]
            rn = random.randint(1, 15)
            kk = QT.iloc[rn+1,count]
            self.Q.setText(kk + qn)
            
            

    def button2Function(self) :
        global count, an, kk ,qch
        if qch>=7 or len(data.성명) <=1 :
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            an = 2
            Que.rd(count,kk,an)
            count+=1
            qch+=1
            qn = QT.iloc[1,count]
            rn = random.randint(1, 15)
            kk = QT.iloc[rn+1,count]
            self.Q.setText(kk + qn)
            
            

    def button3Function(self) :
        global count, an, kk ,qch
        if qch>=7 or len(data.성명) <=1 :
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            an = 3
            Que.rd(count,kk,an)
            count+=1
            qch+=1
            qn = QT.iloc[1,count]
            rn = random.randint(1, 15)
            kk = QT.iloc[rn+1,count]
            self.Q.setText(kk + qn)
            

class AnswerWindow(QMainWindow, aui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(900, 500)
        while qch>=5:
            self.label_2.setText(str(data.성명))
            break


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    widget = QtWidgets.QStackedLayout()

    #WindowClass의 인스턴스 생성
    MainWindow = MainWindow() 
    AnswerWindow = AnswerWindow()

    widget.addWidget(MainWindow)
    widget.addWidget(AnswerWindow)

    #프로그램 화면을 보여주는 코드
    MainWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()