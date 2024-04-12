# ch 5.2.1 ctrl.py
class Control:

    def __init__(self, View):
        self.view = View
        self.connectSignals()

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.activateMessage)
        self.view.btn2.clicked.connect(self.view.clearMessage)