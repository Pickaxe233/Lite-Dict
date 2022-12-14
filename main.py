import json
import requests
import datetime
import sys
import cn2an
import threads
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from borax.calendars.lunardate import LunarDate
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QImage, QPixmap, QFont, QFontDatabase, QCloseEvent
from ui.ui_main import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import Qt, QSize, QUrl
                
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.voice1)
        self.pushButton_3.clicked.connect(self.voice2)
        self.pushButton_4.clicked.connect(lambda:self.pic(0))
        self.pushButton_5.clicked.connect(lambda:self.pic(1))
        self.actionConfigrations.triggered.connect(self.configs)
        self.lineEdit.returnPressed.connect(self.search)
        self.pushButton_10.clicked.connect(self.pgup)
        self.pushButton_8.clicked.connect(self.pgdn)
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
        options = webdriver.EdgeOptions()
        options.add_argument('headless')
        options.add_argument('disable-gpu')
        self.browser = webdriver.Edge(options=options)
        
        self.pushButton_2.setFont(QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont('./font/GentiumPlus-Regular.ttf')))
        self.pushButton_3.setFont(QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont('./font/GentiumPlus-Regular.ttf')))

    def webClose(self):
        self.browser.close()
        self.browser.quit()
        self.Threads.terminate()

    '''def webControl(self,a="",num=4):
        match num:
            case 0:'''
                
        
    def closeEvent(self, a0: QCloseEvent) -> None:
        super().closeEvent(a0)
        self.Threads =  threads.webThread()#t=0,a="")
        self.Threads.finishSignal.connect(self.webClose)
        self.Threads.start()
    
    #????????????
    def ydtran(self,a=""):
        means = requests.get("http://fanyi.youdao.com/openapi.do?keyfrom=neverland&key=969918857&type=data&doctype=json&version=1.1&q="+a)
        json2 = json.loads(means.text)
        if len(json2) == 5: 
            if len(json2['basic']) == 4:          
                a = "BrE:/"+json2['basic']['uk-phonetic']+"/"
                b = "AmE:/"+json2['basic']['us-phonetic']+"/"
                self.pushButton_2.setText(a)
                self.pushButton_2.setEnabled(True)
                self.pushButton_3.setText(b)
                self.pushButton_3.setEnabled(True)
                c = json2['basic']['explains']
                if len(c) > 1:
                    for i in range(len(c)):
                        self.Youdao_Dict.append(c[i])
                else:
                    self.Youdao_Dict.append(c[0])
        else:
            self.Threads =  threads.Thread(t=1)
            self.Threads.finishSignal.connect(self.Change)
            self.Threads.start()

    #????????????
    def bing(self,a=""):
        self.browser.get(f'https://cn.bing.com/dict/search?q={a}')
        elem = self.browser.find_element(By.CLASS_NAME, 'lf_area').get_attribute('outerHTML')
        self.Bing_Dict.setHtml(elem)
    
    #??????    
    def hidi(self,a=""):
        self.browser.get(f'https://dict.cn/{a}')
        elem = self.browser.find_element(By.CLASS_NAME, 'main').get_attribute('outerHTML')
        self.Hi_Dict.setHtml(elem)
    
    #?????????
    def ici(self,a=""):
        self.browser.get(f'https://www.iciba.com/word?w={a}')
        elem = self.browser.find_element(By.CLASS_NAME, 'Content_center__z9WQY').get_attribute('outerHTML')
        self.Jinshan_Dict.setHtml(elem)
    
    def showPic(self):
        if self.checkBox.checkState() == Qt.CheckState.Checked:
            self.label.show()
        elif self.checkBox.checkState() == Qt.CheckState.Unchecked:
            self.label.hide()

    def pgup(self):
        if self.stackedWidget.currentIndex() == 0:
            self.pushButton_10.setEnabled(False)
        else:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1)
            self.pushButton_8.setEnabled(True)
    def pgdn(self):
        if self.stackedWidget.currentIndex() == 1:
            self.pushButton_8.setEnabled(False)
        else:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1)
            self.pushButton_10.setEnabled(True)

    def Change(self, num=3):
        a = ""
        match num:
            case 0:
                a = "??????????????????"
            case 1:
                a = "???????????????"
            case 2:
                a = "???????????????"
        QMessageBox.warning(self, "??????", a, QMessageBox.StandardButton.Yes)
        self.Threads.terminate()
    '''def copy(self, position):
        popMenu = QMenu()
        cpyAct = popMenu.addAction("&Copy")
        hitIndex = self.listWidget.indexAt(position).column()
        if hitIndex > -1:
            action = popMenu.exec(self.listWidget.mapToGlobal(position))
            if action == cpyAct:
                cp = QApplication.clipboard()
                cp.setText(self.listWidget.item(hitIndex).text())

    def copy1(self, position):
        popMenu = QMenu()
        cpyAct = popMenu.addAction("&Copy")
        hitIndex = self.listWidget_2.indexAt(position).row()
        if hitIndex > -1:
            action = popMenu.exec(self.listWidget_2.mapToGlobal(position))
            if action == cpyAct:
                cp = QApplication.clipboard()
                cp.setText(self.listWidget_2.item(hitIndex).text())'''

    '''def copy2(self, position):
        popMenu = QMenu()
        cpyAct = popMenu.addAction("&Copy")
        allAct = popMenu.addAction("Select &All")
        hitIndex = self.textBrowser.toPlainText()
        if hitIndex != None:
            action = popMenu.exec(self.textBrowser.mapToGlobal(position))
            if action == cpyAct:
                cursor = self.textBrowser.textCursor()
                cp = QApplication.clipboard()
                cp.setText(cursor.selectedText())
            elif action == allAct:
                self.textBrowser.selectAll()

    def maxmin(self):
        if self.isMaximized:
            self.maxi'''
                
    def day(self):
        date = datetime.date.today()
        today = LunarDate.from_solar_date(date.year,date.month,date.day)
        data = str(date)
        data = data.replace("-"," ??? ",1)
        data = data.replace("-"," ??? ",1)
        a1 = data+" ???"
        a2 = "??????"+today.cn_year+today.animal+"???"+today.cn_month+"???"+today.cn_day+"???"
        a3 = "??????"+today.gz_year+"???"+today.gz_month+"???"+today.gz_day+"???"
        a = a1+"\t"+a2+"\t"+a3
        self.lineEdit.setPlaceholderText(a)
        return date

    def configs(self):
        self.a = config.Config()
        self.a.show()

    '''def clear(self):
        self.plainTextEdit.clear()
        self.textBrowser.clear()'''

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
                self.Threads = threads.Thread(t=1)
                self.Threads.finishSignal.connect(self.Change)
                self.Threads.start()
            else:
                self.label_2.setText(a)
                self.tabWidget.setCurrentIndex(1)
                if requests.get('https://www.baidu.com').status_code == 200:
                    self.Hi_Dict.clear()
                    self.Youdao_Dict.clear()
                    self.Bing_Dict.clear()
                    self.Jinshan_Dict.clear()
                    self.ydtran(a)
                    self.bing(a)
                    self.ici(a)
                    self.hidi(a)
                else:
                    self.Threads =  threads.Thread(t=2)
                    self.Threads.finishSignal.connect(self.Change)
                    self.Threads.start()  
        else:
            self.Threads = threads.Thread(t=0)
            self.Threads.finishSignal.connect(self.Change)
            self.Threads.start()
            
    '''def translate(self):
        a = "http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i="
        translate = requests.get(a+self.plainTextEdit.toPlainText())
        if self.plainTextEdit.toPlainText() != None:
            if translate.status_code != None:
                json1 = json.loads(translate.text)
                b = json1['translateResult']
                c = len(b[0][0])
                if c == 1:
                    self.textBrowser.setText(b[0][0]['tgt'])
                else:
                    self.textBrowser.clear()
                    for i  in range(0,len(b)):
                        for h in range(0,len(b[i])):
                            self.textBrowser.append(b[i][h]['tgt'])
            else:
                self.thread = Threads.msgThread(t=2)
                self.thread.finishSignal.connect(self.Change)
                self.thread.start()
        else:
            self.thread = Threads.msgThread(t=0)
            self.thread.finishSignal.connect(self.Change)
            self.thread.start()'''

    def pic(self, num):   
        a = "http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title="
        sentence = requests.request('GET',a+str(self.day()))
        if sentence.status_code != None:
            match num:
                case 0:
                    self.thread =  threads.Thread(t=0)
                    self.thread.finishSignal.connect(self.picChange)
                    self.thread.start()
                case 1:
                    self.thread = threads.Thread(t=1)
                    self.thread.finishSignal.connect(self.picChange)
                    self.thread.start()
                case 3:
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
                        self.label_3.setText("Happy Birthday!\n"+b+"??????????????????")
                        self.label_3.setFont(QFont(name[0],10))
                        self.pushButton_4.hide()
                        self.pushButton_5.hide()
                        self.checkBox.hide()
                    else:
                        json1 = json.loads(sentence.text)
                        b = json1['content']+"\n"+json1['note']
                        self.label_3.setText(b)
                        pic2 = json1['picture2'].replace("\\","")
                        res = requests.get(pic2)
                        img = QImage.fromData(res.content)
                        #size = QSize(self.tabWidget.width())
                        self.label.setPixmap(QPixmap.fromImage(img))
                    self.checkBox.setEnabled(True)
                    self.checkBox.setChecked(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_5.setText("?????????")
            self.pushButton_4.setText("?????????")
        else:
            self.thread = threads.Thread(t=2)
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
        self.thread =  threads.Thread(t=0)
        self.thread.finishSignal.connect(self.voice)
        self.thread.start()

    def voice2(self):       
        self.thread =  threads.Thread(t=1)
        self.thread.finishSignal.connect(self.voice)
        self.thread.start()

if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Floor)
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())