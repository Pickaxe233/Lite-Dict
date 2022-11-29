from ui_configs import Ui_Dialog
from PySide6.QtWidgets import QApplication, QDialog, QHeaderView, QTableWidgetItem, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
import sys

class Config(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Config, self).__init__(parent)
        self.setupUi(self)
        
        ckbox = QTableWidgetItem()
        ckbox.setCheckState(Qt.CheckState.Unchecked)
        ckbox.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
        ckbox1 = QTableWidgetItem()
        ckbox1.setCheckState(Qt.CheckState.Checked)
        ckbox1.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
        self.tableWidget_2.setItem(0,0,ckbox)
        self.tableWidget_2.setItem(1,0,ckbox1)
        self.tableWidget_2.horizontalHeader().resizeSection(0,self.tableWidget_2.width()//10)
        self.tableWidget_2.horizontalHeader().resizeSection(1,self.tableWidget_2.width()//6)
        self.tableWidget_2.horizontalHeader().resizeSection(2,self.tableWidget_2.width()//6*2)
        #self.tableWidget_2.cellChanged(0,0).connect(self.apis)

    '''def apis(self):
        1'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Config()
    main_window.show()
    sys.exit(app.exec())