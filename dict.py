# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dict.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 17, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 20, 0, 1, 4)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 23, 3, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.listWidget_2.setFont(font)
        self.listWidget_2.setWordWrap(True)
        self.listWidget_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 18, 2, 2, 2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 17, 8, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 17, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 17, 10, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 17, 9, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 25, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 17, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.listWidget.setFont(font)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setWordWrap(True)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 18, 0, 2, 2)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 16, 8, 1, 3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 17, 6, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 17, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 16, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 18, 6, 1, 5)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 16, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 24, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 19, 6, 8, 5, QtCore.Qt.AlignTop)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 21, 3, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 21, 0, 4, 3)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 22, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        '''self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 22))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.menuOptions.setFont(font)
        self.menuOptions.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.menuOptions.setObjectName("menuOptions")
        self.menuLanguages = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.menuLanguages.setFont(font)
        self.menuLanguages.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.menuLanguages.setObjectName("menuLanguages")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSet_apis = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.actionSet_apis.setFont(font)
        self.actionSet_apis.setObjectName("actionSet_apis")
        self.action = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.action.setFont(font)
        self.action.setObjectName("action")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.actionEnglish.setFont(font)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionPic_sources = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.actionPic_sources.setFont(font)
        self.actionPic_sources.setObjectName("actionPic_sources")
        self.actionFunctions = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("等线")
        self.actionFunctions.setFont(font)
        self.actionFunctions.setObjectName("actionFunctions")
        self.menuOptions.addAction(self.actionSet_apis)
        self.menuOptions.addAction(self.actionPic_sources)
        self.menuOptions.addAction(self.actionFunctions)
        self.menuLanguages.addAction(self.action)
        self.menuLanguages.addAction(self.actionEnglish)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuLanguages.menuAction())'''

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DictionaryForAll"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入要查询的单词"))
        self.checkBox.setText(_translate("MainWindow", "显示图片"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "-"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_5.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_6.setText(_translate("MainWindow", "Translate"))
        self.pushButton_7.setText(_translate("MainWindow", "Clear"))
        '''self.menuOptions.setTitle(_translate("MainWindow", "设置"))
        self.menuLanguages.setTitle(_translate("MainWindow", "语言"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionSet_apis.setText(_translate("MainWindow", "接口设置"))
        self.action.setText(_translate("MainWindow", "简体中文"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionPic_sources.setText(_translate("MainWindow", "图源设置"))
        self.actionFunctions.setText(_translate("MainWindow", "功能设置"))'''
