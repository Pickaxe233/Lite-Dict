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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1231, 571))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_4, 2, 10, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setPointSize(10)
        self.label_3.setFont(font1)
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(3)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 8)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 2, 9, 1, 1, Qt.AlignHCenter)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 11)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setFont(font)

        self.gridLayout_2.addWidget(self.pushButton_5, 2, 8, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 1231, 571))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 0, 0)
        self.listWidget_2 = QListWidget(self.gridLayoutWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setFont(font)
        self.listWidget_2.setWordWrap(True)

        self.gridLayout_3.addWidget(self.listWidget_2, 3, 0, 1, 6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 5, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QSize(150, 0))
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u7ebf"])
        font2.setPointSize(12)
        self.pushButton_2.setFont(font2)

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 3)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamilies([u"\u7b49\u7ebf"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setMargin(10)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 5)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMinimumSize(QSize(150, 0))
        self.pushButton_3.setFont(font2)

        self.gridLayout_3.addWidget(self.pushButton_3, 1, 3, 1, 2)

        self.listWidget = QListWidget(self.gridLayoutWidget_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFont(font)
        self.listWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setWordWrap(True)

        self.gridLayout_3.addWidget(self.listWidget, 2, 0, 1, 6)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(-1, -1, 1231, 571))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 4, 0, 2, 2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 60))
        self.lineEdit.setFont(font2)
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 60))
        self.pushButton.setFont(font)

        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 30))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuOptions.setFont(font)
        self.menuOptions.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.menuLanguages = QMenu(self.menubar)
        self.menuLanguages.setObjectName(u"menuLanguages")
        self.menuLanguages.setFont(font)
        self.menuLanguages.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuLanguages.menuAction())
        self.menuOptions.addAction(self.actionConfigrations)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionAbout)
        self.menuLanguages.addAction(self.action)
        self.menuLanguages.addAction(self.actionEnglish)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


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
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u56fe\u7247", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u67e5\u8be2\u7684\u5355\u8bcd", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuLanguages.setTitle(QCoreApplication.translate("MainWindow", u"Languages", None))
    # retranslateUi

