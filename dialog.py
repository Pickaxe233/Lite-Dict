import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDialog案例")
        self.resize(300, 200)

        # 设置文本内容 + 直接固定到主窗口
        self.button = QPushButton("弹出对话框", self)
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        # 创建对话框控件，并在对话框中创建新的控件
        dialog = QDialog()
        button = QPushButton("确定", dialog)

        # dialog的close方法作用是将对话框关闭
        button.clicked.connect(dialog.close)

        button.move(50, 50)
        dialog.setWindowTitle("对话框")

        # 让对话框以模式的状态显示，即触发对话框后，主窗口的控件时无法使用的
        dialog.setWindowModality(Qt.ApplicationModal)

        # 最后不要忘了调用exec来执行创建的对话框
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())