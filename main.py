import json
import requests
import datetime
import sys
import cn2an
import re
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from borax.calendars.lunardate import LunarDate
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PySide6.QtGui import QImage, QPixmap, QFont, QFontDatabase, QCloseEvent
from ui_main import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import Qt, QSize, QUrl, Signal, QThread

class Thread(QThread):
    finishSignal = Signal(int)

    def __init__(self, t, parent=None):
        super(Thread, self).__init__(parent)
        self.t = t

    def run(self):
        self.finishSignal.emit(int(self.t)) 
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.voice1)
        self.pushButton_3.clicked.connect(self.voice2)
        self.pushButton_4.clicked.connect(lambda:self.pic(0))
        self.pushButton_5.clicked.connect(lambda:self.pic(1))
        self.lineEdit.returnPressed.connect(self.search)
        #self.listWidget.customContextMenuRequested.connect(self.copy)
        #self.listWidget_2.customContextMenuRequested.connect(self.copy1)
        #self.textBrowser.customContextMenuRequested.connect(self.copy2)
        self.checkBox.stateChanged.connect(self.showPic)
        #self.pushButton_6.clicked.connect(self.translate)
        #self.pushButton_7.clicked.connect(self.clear)
        
        self.day()
        self.pic(3)
        
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.audio.setVolume(1)
        self.player.setAudioOutput(self.audio)
        
        self.az = datetime.date.today()
        
        self.pushButton_2.setFont(QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont('./font/GentiumPlus-Regular.ttf')))
        self.pushButton_3.setFont(QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont('./font/GentiumPlus-Regular.ttf')))    
    
    def startCheck(self):
        uri = ["https://dict.youdao.com","https://www.iciba.com","https://www.dict.cn","https://cn.bing.com/dict"]
        uriName = ["Youdao","Iciba","Haici","Bing"]
        for i in range(0,len(uri)):
            code = requests.get(uri[i]).status_code
            if code == 200:
                self.listWidget.addItem(uriName[i])
            else:
                self.Threads = Thread(t=2)
                self.Threads.finishSignal.connect(self.Change)
                self.Threads.start()
                break
    
    def dicts(self):
        query = self.lineEdit.text()
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0"}
        #爱词霸
        res = json.loads(requests.get(f"https://dict.iciba.com/dictionary/word/query/web?client=6&key=1000006&timestamp=1673095657111&word={query}&signature=006872c2788b1e63ec6d9eb922848946",headers=header).text)
        for i in range(0,len())
    
    def showPic(self):
        if self.checkBox.checkState() == Qt.CheckState.Checked:
            self.label.show()
            self.pushButton_5.setEnabled(True)
            self.pushButton_4.setEnabled(True)
        elif self.checkBox.checkState() == Qt.CheckState.Unchecked:
            self.label.hide()
            self.pushButton_5.setEnabled(False)
            self.pushButton_4.setEnabled(False)

    def Change(self, num=3):
        a = ""
        match num:
            case 0:
                a = "输入不能为空"
            case 1:
                a = "请检查拼写"
            case 2:
                a = "请检查网络"
        QMessageBox.warning(self, "错误", a, QMessageBox.StandardButton.Yes)
        self.Threads.terminate()
    
    def day(self):
        date = datetime.date.today()
        today = LunarDate.from_solar_date(date.year,date.month,date.day)
        data = str(date)
        data = data.replace("-"," 年 ",1)
        data = data.replace("-"," 月 ",1)
        a1 = data+" 日"
        a2 = "农历"+today.cn_year+today.animal+"年"+today.cn_month+"月"+today.cn_day+"日"
        a3 = "干支"+today.gz_year+"年"+today.gz_month+"月"+today.gz_day+"日"
        a = a1+"\t"+a2+"\t"+a3
        self.lineEdit.setPlaceholderText(a)
        return date

    def picChange(self, num):
        m = "http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title="
        match num:
            case 0:
                self.az += datetime.timedelta(days=1)
                if self.az != self.day():
                    self.pushButton_4.setEnabled(True)
                else:
                    self.pushButton_4.setEnabled(False)
            case 1:
                self.az -= datetime.timedelta(days=1)
                self.pushButton_4.setEnabled(True)
        pic = requests.request('GET',m+str(self.az))
        json1 = json.loads(pic.text)
        b = json1['content']+"\n"+json1['note']
        self.label_3.setText(b)
        pic2 = json1['picture2'].replace("\\","")
        res = requests.get(pic2)
        img = QImage.fromData(res.content)
        self.label.setPixmap(QPixmap.fromImage(img))
        self.thread.terminate()

    def search(self):
        a = self.lineEdit.text()
        if a != "":
            if re.match('[^a-zA-Z]', a):
                self.Threads = Thread(t=1)
                self.Threads.finishSignal.connect(self.Change)
                self.Threads.start()
            else:
                self.label_2.setText(a)
                self.tabWidget.setCurrentIndex(1)
        else:
            self.Threads = Thread(t=0)
            self.Threads.finishSignal.connect(self.Change)
            self.Threads.start()

    def pic(self, num):   
        uri = "http://open.iciba.com/dsapi/"
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0"}
        sentence = requests.request('GET',uri+str(self.day()),headers=header)
        if sentence.status_code != None:
            if self.day().month == 11 and self.day().day == 24:
                id = QFontDatabase.addApplicationFont('./font/Minecraft_AE.ttf')
                name = QFontDatabase.applicationFontFamilies(id)
                self.label_3.setFont(QFont(name[0],10))
                b = cn2an.an2cn(int(self.day().year) - 2006)
                pic = requests.request('GET',"https://static.wikia.nocookie.net/minecraft_zh_gamepedia/images/4/4c/Candle_Cake.png/revision/latest?cb=20201112035153")
                img = QImage.fromData(pic.content)
                size = QSize(img.width(),img.height())
                pix = QPixmap.fromImage(img.scaled(size, Qt.AspectRatioMode.KeepAspectRatio))
                self.label.setScaledContents(False)
                self.label.setPixmap(pix)
                self.label_3.setText("Happy Birthday!\n"+b+"岁生日快乐！")
                self.label_3.setFont(QFont(name[0],10))
                self.pushButton_4.hide()
                self.pushButton_5.hide()
                self.checkBox.hide()
            else:
                json1 = json.loads(sentence.text)
                b = json1['content']+"\n"+json1['note']
                self.label_3.setText(b)
                res = requests.get(json1['picture4'])
                img = QImage.fromData(res.content)
                self.label.setPixmap(QPixmap.fromImage(img))
            self.checkBox.setEnabled(True)
            self.checkBox.setChecked(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_5.setText("上一张")
            self.pushButton_4.setText("下一张")
        else:
            self.thread = Thread(t=2)
            self.thread.finishSignal.connect(self.Change)
            self.thread.start()
                 
    def voice(self,num):
        a = ""
        match num:
            case 0:
                a = "http://dict.youdao.com/dictvoice?type=1&audio="
            case 1:
                a = "http://dict.youdao.com/dictvoice?type=0&audio="
        self.player.setSource(QUrl(a+self.lineEdit.text()))
        self.player.play()
        self.thread.terminate()

    def voice1(self):
        self.thread =  Thread(t=0)
        self.thread.finishSignal.connect(self.voice)
        self.thread.start()

    def voice2(self):       
        self.thread =  Thread(t=1)
        self.thread.finishSignal.connect(self.voice)
        self.thread.start()

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Floor)
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())