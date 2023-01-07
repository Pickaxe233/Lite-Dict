from PySide6.QtCore import QThread, Signal

class Thread(QThread):
    finishSignal = Signal(int)

    def __init__(self, t, parent=None):
        super(Thread, self).__init__(parent)
        self.t = t

    def run(self):
        self.finishSignal.emit(int(self.t)) 

'''class webThread(QThread):
    finishSignal = Signal()

    def __init__(self, t, a, parent=None):
        super(webThread, self).__init__(parent)
        self.t = t
        self.a = a

    def run(self):
        self.finishSignal.emit(int(self.t))
        self.finishSignal.emit(str(self.a))'''
        
class webThread(QThread):
    finishSignal = Signal()

    def __init__(self, parent=None):
        super(webThread, self).__init__(parent)

    def run(self):
        self.finishSignal.emit()