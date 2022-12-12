# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configs.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QAbstractScrollArea, QApplication,
    QCheckBox, QComboBox, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QHeaderView, QLineEdit,
    QRadioButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(720, 480)
        Dialog.setMinimumSize(QSize(720, 480))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        Dialog.setFont(font)
        Dialog.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_2 = QTableWidget(self.tab)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setKerning(True)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget_2.rowCount() < 2):
            self.tableWidget_2.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font);
        __qtablewidgetitem5.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font);
        __qtablewidgetitem7.setFlags(Qt.NoItemFlags);
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font);
        __qtablewidgetitem8.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font);
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFlags(Qt.NoItemFlags);
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tableWidget_2, 1, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 651, 351))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolButton_2 = QToolButton(self.gridLayoutWidget_2)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.gridLayout_3.addWidget(self.toolButton_2, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.tableWidget_3 = QTableWidget(self.gridLayoutWidget_2)
        if (self.tableWidget_3.columnCount() < 4):
            self.tableWidget_3.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font);
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        if (self.tableWidget_3.rowCount() < 2):
            self.tableWidget_3.setRowCount(2)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem16)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.tableWidget_3, 2, 0, 1, 7)

        self.toolButton = QToolButton(self.gridLayoutWidget_2)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_3.addWidget(self.toolButton, 3, 2, 1, 5)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(9, 9, 671, 221))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.checkBox_2 = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_4.addWidget(self.checkBox_2, 0, 3, 1, 2)

        self.comboBox = QComboBox(self.gridLayoutWidget_3)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 4, 0, 1, 2)

        self.checkBox = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_4.addWidget(self.checkBox, 0, 0, 1, 2)

        self.radioButton_2 = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_4.addWidget(self.radioButton_2, 5, 0, 1, 2)

        self.radioButton = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_4.addWidget(self.radioButton, 2, 0, 1, 2)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 6, 0, 1, 1)

        self.toolButton_7 = QToolButton(self.gridLayoutWidget_3)
        self.toolButton_7.setObjectName(u"toolButton_7")

        self.gridLayout_4.addWidget(self.toolButton_7, 6, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_4.addWidget(self.checkBox_3, 1, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 7, 0, 2, 2)

        self.radioButton_3 = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_4.addWidget(self.radioButton_3, 1, 3, 1, 2)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_4.addWidget(self.comboBox_2, 2, 3, 1, 2)

        self.radioButton_4 = QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_4.addWidget(self.radioButton_4, 4, 3, 1, 2)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 5, 3, 1, 1)

        self.toolButton_8 = QToolButton(self.gridLayoutWidget_3)
        self.toolButton_8.setObjectName(u"toolButton_8")

        self.gridLayout_4.addWidget(self.toolButton_8, 5, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 6, 3, 3, 2)

        self.tabWidget.addTab(self.tab_3, "")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.tabWidget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configrations", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"key", None));
        ___qtablewidgetitem3 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"1", None));
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"2", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u6709\u9053\u8bcd\u5178", None));
        ___qtablewidgetitem6 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"-", None));
        ___qtablewidgetitem7 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"\u6709\u9053\u7ffb\u8bd1", None));
        ___qtablewidgetitem8 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"-", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"\u8bcd\u5178", None))
        self.toolButton_2.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0", None))
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"key", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"\u94fe\u63a5", None));
        ___qtablewidgetitem13 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"1", None));
        ___qtablewidgetitem14 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"2", None));
        self.toolButton.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"\u7ffb\u8bd1", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"\u6bcf\u65e5\u4e00\u53e5", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u6bcf\u65e5\u4e00\u56fe", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"\u81ea\u5b9a\u4e49\u56fe\u7247", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\u5185\u7f6e", None))
        self.toolButton_7.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u529f\u80fd", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"\u5185\u7f6e", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"\u81ea\u5b9a\u4e49\u6587\u672c", None))
        self.toolButton_8.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"\u56fe\u53e5", None))
    # retranslateUi

