import json
import requests
import datetime
import sys
import re
import cn2an
import Threads
import config
from borax.calendars.lunardate import LunarDate
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QMenu
from PySide6.QtGui import QImage, QPixmap, QFont, QFontDatabase
from ui_dict import Ui_MainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaDevices, QAudioDevice
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
        self.listWidget.customContextMenuRequested.connect(self.copy)
        self.listWidget_2.customContextMenuRequested.connect(self.copy1)
        self.textBrowser.customContextMenuRequested.connect(self.copy2)
        self.checkBox.stateChanged.connect(lambda:self.pic(2))
        self.pushButton_6.clicked.connect(self.translate)
        self.pushButton_7.clicked.connect(self.clear)
        self.comboBox.hide()
        self.comboBox_2.hide()
        
        self.day()
        self.pic(3)
        
        self.az = datetime.date.today()

    def copy(self, position):
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
                cp.setText(self.listWidget_2.item(hitIndex).text())

    def copy2(self, position):
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

                
    def day(self):
        date = datetime.date.today()
        today = LunarDate.from_solar_date(date.year,date.month,date.day)
        data = str(date)
        data = data.replace("-"," 年 ",1)
        data = data.replace("-"," 月 ",1)
        a1 = data+" 日"
        a2 = "农历"+today.cn_year+today.animal+"年"+today.cn_month+"月"+today.cn_day+"日"
        a3 = "干支"+today.gz_year+"年"+today.gz_month+"月"+today.gz_day+"日"
        a = a1+"\n"+a2+"\n"+a3
        self.label_2.setText(a)
        return date

    def configs(self):
        self.a = config.Config()
        self.a.show()

    def clear(self):
        self.plainTextEdit.clear()
        self.textBrowser.clear()

    def Change(self, num):
        a = ""
        match num:
            case 0:
                a = "输入不能为空"
            case 1:
                a = "请检查拼写"
            case 2:
                a = "请检查网络"
        QMessageBox.warning(self, "错误", a, QMessageBox.StandardButton.Yes)
        self.thread.terminate()

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
        size = QSize(int(img.width()*0.5),int(img.height()*0.5),)
        self.label.setPixmap(QPixmap.fromImage(img.scaled(size,Qt.AspectRatioMode.KeepAspectRatio)))
        self.thread.terminate()
                
    def search(self):
        a = self.lineEdit.text()
        if a != "":
            means = requests.get("http://fanyi.youdao.com/openapi.do?keyfrom=neverland&key=969918857&type=data&doctype=json&version=1.1&q="+a)
            if means.status_code != None:
                json2 = json.loads(means.text)
                if re.match('[^a-zA-Z]', a):
                    self.thread = Threads.msgThread(t=1)
                    self.thread.finishSignal.connect(self.Change)
                    self.thread.start()
                else:
                    if len(json2) == 5: 
                        self.listWidget.clear()
                        self.listWidget.scrollToTop()
                        if len(json2['basic']) == 4:
                            a = "英音：/"+json2['basic']['uk-phonetic']+"/"
                            b = "美音：/"+json2['basic']['us-phonetic']+"/"
                            self.pushButton_2.setText(a)
                            self.pushButton_2.setEnabled(True)
                            self.pushButton_3.setText(b)
                            self.pushButton_3.setEnabled(True)
                            c = json2['basic']['explains']
                            if len(c[0].split(".",1)) > 1:
                                for i in range(0,len(c)):
                                    d = c[i].split(".")
                                    for h ,f in zip(range(0,len(d)//2), range(0,len(d)//2+1)):
                                        e = d[f*2-1].split("；")
                                        for z in range(0,len(e)):
                                            self.listWidget.addItem(d[2*h]+". "+e[z])
                                if c[-1].find("【") != -1:
                                    self.listWidget.addItem(c[-1])
                            else:
                                self.listWidget.addItem(c[0])
                        if len(json2) > 3:                                  
                            self.listWidget_2.clear()
                            self.listWidget_2.scrollToTop()     
                            for i in range(0,len(json2['web'])):
                                self.listWidget_2.addItem(json2['web'][i]['key']+":")
                                for h in range(0,len(json2['web'][i]['value'])):
                                    self.listWidget_2.addItem((json2['web'][i]['value'][h]))     
                    else:
                        self.thread =  Threads.msgThread(t=1)
                        self.thread.finishSignal.connect(self.Change)
                        self.thread.start()
            else:
                self.thread =  Threads.msgThread(t=2)
                self.thread.finishSignal.connect(self.Change)
                self.thread.start()   
        else:
            self.thread = Threads.msgThread(t=0)
            self.thread.finishSignal.connect(self.picChange)
            self.thread.start()

    def translate(self):
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
            self.thread.start()

    def pic(self, num):   
        a = "http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title="
        sentence = requests.request('GET',a+str(self.day()))
        if sentence.status_code != None:
            match num:
                case 0:
                    self.thread =  Threads.picThread(t=0)
                    self.thread.finishSignal.connect(self.picChange)
                    self.thread.start()
                case 1:
                    self.thread = Threads.picThread(t=1)
                    self.thread.finishSignal.connect(self.picChange)
                    self.thread.start()
                case 2:
                    if self.checkBox.checkState() == Qt.CheckState.Checked:
                        self.label.show()
                    elif self.checkBox.checkState() == Qt.CheckState.Unchecked:
                        self.label.hide()
                case 3:
                    if self.day().month == 11 and self.day().day == 24:
                        id = QFontDatabase.addApplicationFont('./Minecraft_AE.ttf')
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
                        pic2 = json1['picture2'].replace("\\","")
                        res = requests.get(pic2)
                        img = QImage.fromData(res.content)
                        size = QSize(int(img.width()*0.5),int(img.height()*0.5),)
                        self.label.setPixmap(QPixmap.fromImage(img.scaled(size,Qt.AspectRatioMode.KeepAspectRatio)))
                    self.checkBox.setEnabled(True)
                    self.checkBox.setChecked(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_5.setText("上一张")
            self.pushButton_4.setText("下一张")
        else:
            self.thread = Threads.msgThread(t=2)
            self.thread.finishSignal.connect(self.Change)
            self.thread.start()
                 
    def voice(self,num):
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.audio.setDevice(QMediaDevices.defaultAudioOutput())
        self.audio.setVolume(100)
        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(100)
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
        self.thread =  Threads.voiceThread(t=0)
        self.thread.finishSignal.connect(self.voice)
        self.thread.start()

    def voice2(self):       
        self.thread =  Threads.voiceThread(t=1)
        self.thread.finishSignal.connect(self.voice)
        self.thread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())