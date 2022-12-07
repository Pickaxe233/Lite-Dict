# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dict.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QSize(1080, 720))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionSet_apis = QAction(MainWindow)
        self.actionSet_apis.setObjectName(u"actionSet_apis")
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        self.actionSet_apis.setFont(font)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action.setFont(font)
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionEnglish.setFont(font)
        self.actionPic_sources = QAction(MainWindow)
        self.actionPic_sources.setObjectName(u"actionPic_sources")
        self.actionPic_sources.setFont(font)
        self.actionFunctions = QAction(MainWindow)
        self.actionFunctions.setObjectName(u"actionFunctions")
        self.actionFunctions.setFont(font)
        self.actionConfigrations = QAction(MainWindow)
        self.actionConfigrations.setObjectName(u"actionConfigrations")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(150, 0))
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit, 18, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 26, 3, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 18, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setFont(font)

        self.gridLayout.addWidget(self.pushButton_4, 18, 9, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 22, 0, 1, 4)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setFont(font)

        self.gridLayout.addWidget(self.checkBox, 18, 8, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)

        self.gridLayout.addWidget(self.pushButton_7, 24, 3, 1, 1)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFont(font)
        self.listWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setWordWrap(True)

        self.gridLayout.addWidget(self.listWidget, 20, 0, 2, 2)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 23, 0, 4, 3)

        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setFont(font)
        self.listWidget_2.setWordWrap(True)

        self.gridLayout.addWidget(self.listWidget_2, 20, 2, 2, 2)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setFont(font)

        self.gridLayout.addWidget(self.pushButton_5, 18, 6, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 18, 10, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setOpenLinks(False)

        self.gridLayout.addWidget(self.textBrowser, 27, 0, 1, 4)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 25, 3, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font)

        self.gridLayout.addWidget(self.pushButton_6, 23, 3, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)

        self.gridLayout.addWidget(self.label_3, 20, 6, 1, 5)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMinimumSize(QSize(150, 0))
        self.pushButton_3.setFont(font)

        self.gridLayout.addWidget(self.pushButton_3, 18, 2, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 21, 6, 8, 5, Qt.AlignTop)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 17, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QSize(150, 0))
        self.pushButton_2.setFont(font)

        self.gridLayout.addWidget(self.pushButton_2, 17, 2, 1, 2, Qt.AlignBottom)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.label_2, 17, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 22))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuOptions.setFont(font)
        self.menuOptions.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        #self.menuLanguages = QMenu(self.menubar)
        #self.menuLanguages.setObjectName(u"menuLanguages")
        #self.menuLanguages.setFont(font)
        #self.menuLanguages.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())
        #self.menubar.addAction(self.menuLanguages.menuAction())
        self.menuOptions.addAction(self.actionConfigrations)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionAbout)
        #self.menuLanguages.addAction(self.action)
        #self.menuLanguages.addAction(self.actionEnglish)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DictionaryForAll", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionSet_apis.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u53e3\u8bbe\u7f6e", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionPic_sources.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u6e90\u8bbe\u7f6e", None))
        self.actionFunctions.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u8bbe\u7f6e", None))
        self.actionConfigrations.setText(QCoreApplication.translate("MainWindow", u"Configrations", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u67e5\u8be2\u7684\u5355\u8bcd", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u56fe\u7247", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        #self.menuLanguages.setTitle(QCoreApplication.translate("MainWindow", u"Languages", None))
    # retranslateUi

