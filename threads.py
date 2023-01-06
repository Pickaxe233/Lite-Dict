from PySide6.QtCore import QThread, Signal

class msgThread(QThread):
    finishSignal = Signal(int)

    def __init__(self, t, parent=None):
        super(msgThread, self).__init__(parent)
        self.t = t

    def run(self):
        self.finishSignal.emit(int(self.t)) 

class voiceThread(QThread):
    finishSignal = Signal(int)

    def __init__(self, t, parent=None):
        super(voiceThread, self).__init__(parent)
        self.t = t

    def run(self):
        self.finishSignal.emit(int(self.t))

class picThread(QThread):
    finishSignal = Signal(int)

    def __init__(self, t, parent=None):
        super(picThread, self).__init__(parent)
        self.t = t

    def run(self):
        self.finishSignal.emit(int(self.t))
        
class webThread(QThread):
    finishSignal = Signal()

    def __init__(self, parent=None):
        super(webThread, self).__init__(parent)

    def run(self):
        self.finishSignal.emit()