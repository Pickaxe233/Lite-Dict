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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
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
        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 1, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 2)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setFont(font2)

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"\u7b49\u7ebf"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setUnderline(False)
        self.label_3.setFont(font3)
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(3)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 3, 2)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(False)

        self.gridLayout_2.addWidget(self.pushButton_9, 1, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setFont(font2)

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 1551, 791))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.gridLayoutWidget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayoutWidget_5 = QWidget(self.page)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 1281, 641))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayoutWidget_2 = QWidget(self.page_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 1281, 641))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_3.addWidget(self.stackedWidget, 4, 0, 1, 5)

        self.listWidget = QListWidget(self.gridLayoutWidget_2)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(40, 0))

        self.gridLayout_3.addWidget(self.listWidget, 4, 5, 1, 1, Qt.AlignRight)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QSize(150, 0))
        font4 = QFont()
        font4.setFamilies([u"\u7b49\u7ebf"])
        font4.setPointSize(15)
        font4.setUnderline(False)
        self.pushButton_2.setFont(font4)

        self.gridLayout_3.addWidget(self.pushButton_2, 2, 0, 2, 2)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setFamilies([u"\u7b49\u7ebf"])
        font5.setPointSize(45)
        font5.setBold(True)
        font5.setUnderline(False)
        self.label_2.setFont(font5)
        self.label_2.setMargin(10)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 6)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMinimumSize(QSize(150, 0))
        self.pushButton_3.setFont(font4)

        self.gridLayout_3.addWidget(self.pushButton_3, 2, 2, 2, 2)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        font6 = QFont()
        font6.setFamilies([u"\u7b49\u7ebf"])
        font6.setPointSize(12)
        font6.setUnderline(False)
        self.label_9.setFont(font6)

        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 4, 3, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(9, -1, 1521, 761))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(15)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.checkBox_3 = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_4.addWidget(self.checkBox_3, 4, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_4.addWidget(self.pushButton_7, 1, 2, 1, 1, Qt.AlignLeft)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_6, 0, 2, 1, 1, Qt.AlignLeft)

        self.comboBox = QComboBox(self.gridLayoutWidget_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 5, 2, 1, 1, Qt.AlignLeft)

        self.textBrowser_3 = QTextBrowser(self.gridLayoutWidget_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.gridLayout_4.addWidget(self.textBrowser_3, 3, 0, 4, 2)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_4.addWidget(self.pushButton_8, 3, 2, 1, 1, Qt.AlignLeft)

        self.plainTextEdit = QPlainTextEdit(self.gridLayoutWidget_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_4.addWidget(self.plainTextEdit, 0, 0, 3, 2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayoutWidget = QWidget(self.tab_4)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 1521, 761))
        self.gridLayout_7 = QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font4)
        self.groupBox_2.setFlat(True)
        self.gridLayoutWidget_6 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 10, 501, 741))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_8.setSpacing(7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(7, 10, 7, 0)
        self.label_10 = QLabel(self.gridLayoutWidget_6)
        self.label_10.setObjectName(u"label_10")
        font7 = QFont()
        font7.setFamilies([u"\u7b49\u7ebf"])
        font7.setPointSize(10)
        font7.setUnderline(False)
        self.label_10.setFont(font7)

        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.tableWidget = QTableWidget(self.gridLayoutWidget_6)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_8.addWidget(self.tableWidget, 1, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget_6)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font7)

        self.gridLayout_8.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font7)

        self.gridLayout_8.addWidget(self.label_11, 2, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.gridLayoutWidget_6)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setFont(font7)

        self.gridLayout_8.addWidget(self.comboBox_4, 2, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font4)
        self.groupBox.setFlat(True)
        self.gridLayoutWidget_4 = QWidget(self.groupBox)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 10, 501, 741))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setSpacing(7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(7, 10, 7, 0)
        self.imageAutoSaveCheckBox = QCheckBox(self.gridLayoutWidget_4)
        self.imageAutoSaveCheckBox.setObjectName(u"imageAutoSaveCheckBox")
        self.imageAutoSaveCheckBox.setFont(font7)

        self.gridLayout_5.addWidget(self.imageAutoSaveCheckBox, 3, 2, 1, 1)

        self.fontComboBox = QFontComboBox(self.gridLayoutWidget_4)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setFont(font7)

        self.gridLayout_5.addWidget(self.fontComboBox, 8, 2, 1, 1)

        self.imageSouceComboBox = QComboBox(self.gridLayoutWidget_4)
        self.imageSouceComboBox.addItem("")
        self.imageSouceComboBox.addItem("")
        self.imageSouceComboBox.addItem("")
        self.imageSouceComboBox.addItem("")
        self.imageSouceComboBox.addItem("")
        self.imageSouceComboBox.setObjectName(u"imageSouceComboBox")
        self.imageSouceComboBox.setFont(font7)

        self.gridLayout_5.addWidget(self.imageSouceComboBox, 0, 2, 1, 1)

        self.imageLocationLineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.imageLocationLineEdit.setObjectName(u"imageLocationLineEdit")
        self.imageLocationLineEdit.setFont(font7)

        self.gridLayout_5.addWidget(self.imageLocationLineEdit, 2, 2, 1, 1)

        self.fontSizeSlider = QSlider(self.gridLayoutWidget_4)
        self.fontSizeSlider.setObjectName(u"fontSizeSlider")
        self.fontSizeSlider.setMaximum(20)
        self.fontSizeSlider.setSliderPosition(12)
        self.fontSizeSlider.setOrientation(Qt.Horizontal)
        self.fontSizeSlider.setInvertedAppearance(False)
        self.fontSizeSlider.setTickPosition(QSlider.TicksAbove)
        self.fontSizeSlider.setTickInterval(2)

        self.gridLayout_5.addWidget(self.fontSizeSlider, 10, 2, 1, 1)

        self.textSourceComboBox = QComboBox(self.gridLayoutWidget_4)
        self.textSourceComboBox.addItem("")
        self.textSourceComboBox.addItem("")
        self.textSourceComboBox.addItem("")
        self.textSourceComboBox.addItem("")
        self.textSourceComboBox.setObjectName(u"textSourceComboBox")
        self.textSourceComboBox.setFont(font7)

        self.gridLayout_5.addWidget(self.textSourceComboBox, 5, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font7)
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_4, 6, 2, 1, 1)

        self.imageUriLineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.imageUriLineEdit.setObjectName(u"imageUriLineEdit")
        self.imageUriLineEdit.setFont(font7)
        self.imageUriLineEdit.setFrame(True)
        self.imageUriLineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.imageUriLineEdit, 1, 2, 1, 1)

        self.line = QFrame(self.gridLayoutWidget_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_5.addWidget(self.line, 4, 0, 1, 3)

        self.fontLocalLineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.fontLocalLineEdit.setObjectName(u"fontLocalLineEdit")
        self.fontLocalLineEdit.setFont(font7)
        self.fontLocalLineEdit.setReadOnly(True)
        self.fontLocalLineEdit.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.fontLocalLineEdit, 9, 2, 1, 1)

        self.fontSystemComboBox = QComboBox(self.gridLayoutWidget_4)
        self.fontSystemComboBox.addItem("")
        self.fontSystemComboBox.addItem("")
        self.fontSystemComboBox.setObjectName(u"fontSystemComboBox")
        self.fontSystemComboBox.setFont(font7)

        self.gridLayout_5.addWidget(self.fontSystemComboBox, 7, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 11, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)

        self.gridLayout_5.addWidget(self.label_8, 10, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)

        self.gridLayout_5.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font7)

        self.gridLayout_5.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.gridLayout_5.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")
        font8 = QFont()
        font8.setFamilies([u"\u7b49\u7ebf"])
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setUnderline(False)
        self.label_4.setFont(font8)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font4)
        self.groupBox_3.setFlat(True)
        self.gridLayoutWidget_7 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(-1, 10, 501, 741))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_9.setSpacing(7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(7, 10, 7, 0)
        self.groupBox_4 = QGroupBox(self.gridLayoutWidget_7)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font7)
        self.gridLayoutWidget_8 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(-1, 10, 491, 351))
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(5, 5, 5, 0)
        self.checkBox_4 = QCheckBox(self.gridLayoutWidget_8)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_10.addWidget(self.checkBox_4, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.gridLayoutWidget_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setFont(font7)

        self.gridLayout_9.addWidget(self.groupBox_5, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 4, 0, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_6.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DictionaryForAll", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u67e5\u8be2\u7684\u5355\u8bcd", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u56fe\u7247", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Dict", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Show multiple translation", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Baidu", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Youdao", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Sogou", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"DeepL", None))

        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Pronounce", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Translator", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Interfaces", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"API Mode", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Dict Key", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Translator Key", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Bing", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Youdao", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Baidu", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"-", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Web", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Key", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Browser", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Pronunciation Source", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Youdao", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Iciba", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Haici", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Baidu", None))

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Homepage", None))
        self.imageAutoSaveCheckBox.setText(QCoreApplication.translate("MainWindow", u"Image Autosave", None))
        self.imageSouceComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Iciba", None))
        self.imageSouceComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Bing", None))
        self.imageSouceComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Haici", None))
        self.imageSouceComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Youdao", None))
        self.imageSouceComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Other", None))

        self.imageLocationLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click to select", None))
        self.textSourceComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Iciba", None))
        self.textSourceComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Youdao", None))
        self.textSourceComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Haici", None))
        self.textSourceComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-", None))
        self.imageUriLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input URI, file path or right click to select", None))
        self.fontLocalLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click to select", None))
        self.fontSystemComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"System Internal", None))
        self.fontSystemComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Text Size", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Text Font", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Text Sources", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Image Save Location", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Image Sources", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Dictionaries", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Online", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Show Web Explains", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Local", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

