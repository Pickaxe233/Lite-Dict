# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTextBrowser, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QSize(1600, 900))
        MainWindow.setMaximumSize(QSize(1600, 900))
        MainWindow.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 0)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 60))
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u7ebf"])
        font2.setUnderline(False)
        self.tabWidget.setFont(font2)
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1551, 781))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"\u7b49\u7ebf"])
        font3.setPointSize(10)
        font3.setUnderline(False)
        self.label_3.setFont(font3)
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(3)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 8)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 11)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setFont(font2)

        self.gridLayout_2.addWidget(self.pushButton_4, 2, 10, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 2, 9, 1, 1, Qt.AlignHCenter)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setFont(font2)

        self.gridLayout_2.addWidget(self.pushButton_5, 2, 8, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 11)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 1551, 791))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMinimumSize(QSize(150, 0))
        font4 = QFont()
        font4.setFamilies([u"\u7b49\u7ebf"])
        font4.setPointSize(15)
        font4.setUnderline(False)
        self.pushButton_3.setFont(font4)

        self.gridLayout_3.addWidget(self.pushButton_3, 1, 2, 2, 2)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setFamilies([u"\u7b49\u7ebf"])
        font5.setPointSize(45)
        font5.setBold(True)
        font5.setUnderline(False)
        self.label_2.setFont(font5)
        self.label_2.setMargin(10)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 4)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QSize(150, 0))
        self.pushButton_2.setFont(font4)

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 2, 2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 4, 2, 1)

        self.groupBox = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFont(font3)
        self.gridLayoutWidget_4 = QWidget(self.groupBox)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 10, 1541, 691))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 0)
        self.label_6 = QLabel(self.gridLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 0, 2, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_5 = QLabel(self.gridLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")
        font6 = QFont()
        font6.setFamilies([u"\u7b49\u7ebf"])
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setUnderline(True)
        self.label_4.setFont(font6)
        self.label_4.setMargin(1)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_7 = QLabel(self.gridLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 3, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.textBrowser = QTextBrowser(self.gridLayoutWidget_4)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_5.addWidget(self.textBrowser, 1, 0, 1, 5)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget_4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBox_2, 0, 5, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 3, 0, 1, 5)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(9, -1, 1521, 761))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_4.addWidget(self.comboBox_2, 0, 4, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.toolButton = QToolButton(self.gridLayoutWidget_3)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_4.addWidget(self.toolButton, 0, 3, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_3)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 0, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_4.addWidget(self.pushButton_7, 0, 7, 1, 1)

        self.comboBox_4 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_4.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_4.addWidget(self.pushButton_6, 0, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 8, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 2, 0, 1, 9)

        self.plainTextEdit = QPlainTextEdit(self.gridLayoutWidget_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_4.addWidget(self.plainTextEdit, 1, 0, 1, 5)

        self.textBrowser_3 = QTextBrowser(self.gridLayoutWidget_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.gridLayout_4.addWidget(self.textBrowser_3, 1, 5, 1, 5)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 4, 0, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DictionaryForAll", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u67e5\u8be2\u7684\u5355\u8bcd", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u56fe\u7247", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Online Dictionary", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Dict", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Translator", None))
    # retranslateUi

