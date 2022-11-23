import time
from PyQt5.QtCore import QThread, pyqtSignal

class msgThread(QThread):
    finishSignal = pyqtSignal(int)

    def __init__(self, t, parent=None):
        super(msgThread, self).__init__(parent)
        self.t = t

    def run(self):
        self.finishSignal.emit(int(self.t)) 

class voiceThread(QThread):
    finishSignal = pyqtSignal(int)

    def __init__(self, t, parent=None):
        super(voiceThread, self).__init__(parent)
        self.t = t

    def run(self):
        self.finishSignal.emit(int(self.t))

class picThread(QThread):
    finishSignal = pyqtSignal(int)

    def __init__(self, t, parent=None):
        super(picThread, self).__init__(parent)
        self.t = t

    def run(self):
        self.finishSignal.emit(int(self.t))