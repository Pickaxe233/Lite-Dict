from configs import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog
import sys

class Config(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Config, self).__init__(parent)
        self.setupUi(self)

        self.label_2.setHidden(True)
        self.toolButton_4.setHidden(True)
        self.toolButton_3.setHidden(True)
        self.tableWidget.setHidden(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Config()
    main_window.show()
    sys.exit(app.exec_())