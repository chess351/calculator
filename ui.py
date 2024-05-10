# ch 6.2.1 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit, QHBoxLayout,
                             QLineEdit, QComboBox)  # 추가
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore  # 추가


class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()  # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True)  # 텍스트 위젯을 읽기만 가능하도록 수정

        self.btn1 = QPushButton('Message', self)  # 버튼
        self.btn2 = QPushButton('Clear', self)  # 버튼 2

        self.le1 = QLineEdit('0', self)  # 라인 에디트1 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight)  # 라인 에디트1 문자열 배치 설정

        self.le2 = QLineEdit('0', self)  # 라인 에디트2 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight)  # 라인 에디트2 문자열 배치 설정

        self.cb = QComboBox(self)  # 콤보 박스 추가
        self.cb.addItems(['+', '-', '*', '/'])  # 콤보 박스 항목 추가(연산자로 사용)

        hbox_formular = QHBoxLayout()  # 새로 정의한 위젯을 QHBoxLatout에 배치
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.le2)
        hbox_formular.addWidget(self.cb)

        hbox = QHBoxLayout()  # 수평 박스 레이아웃을 추가하고 버튼 1, 2
        hbox.addStretch(1)  # 공백
        hbox.addWidget(self.btn1)  # 버튼 1 배치
        hbox.addWidget(self.btn2)  # 버튼 2 배치

        vbox = QVBoxLayout()  # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)  # 수직 레이아웃에 텍스트 에디트 위젯
        vbox.addLayout(hbox_formular)  # hbox_formular배치
        vbox.addLayout(hbox)  # btn1 위치에 hbox를 배치
        vbox.addStretch(1)  # 빈 공간

        self.setLayout(vbox)  # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))  # 윈도우 아이콘 추가
        self.resize(256,256)
        self.show()
    
    def clearMessage(self):  # 버튼 2 핸들러 함수 정의
        self.te1.clear()

    def activateMessage(self):  # 핸들러 함수 수정 : 메시지가 텍스트 에디트에 출력되도록
        # QMessageBox.information(self,"information","Button clicked!")
        self.te1.appendPlainText("button clicked!")
