# ch 4.2.1 main.py
import sys
from ui import View  # ui.py의 View클래스 추가
from ctrl import Control  # ctrl.py의 Control클래스를 추가
from PyQt5.QtWidgets import QApplication


def main():  # 프로그램 실행(Application) 관련 내용 함수화
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View()  # View 인스턴스 선언
    Control(View=view)  # Control 인스턴스 선언
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()