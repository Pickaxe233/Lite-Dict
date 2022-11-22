import json
import requests
import datetime
from borax.calendars.lunardate import LunarDate
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5.QtGui import QImage, QPixmap
from dict import Ui_MainWindow
from Threads import msgThread, voiceThread
from apis import Ui_Dialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QEvent
import re
#import platform

class Dialog(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

        #self.buttonBox.accepted.connect(self.save)

    '''def save(self):
        if self.buttonBox.accepted'''
                
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.voice1)
        self.pushButton_3.clicked.connect(self.voice2)
        self.actionSet_apis.triggered.connect(self.setApis)
        self.lineEdit.returnPressed.connect(self.search)
        
        date = datetime.date.today()
        data = str(date)
        today = LunarDate.from_solar_date(date.year,date.month,date.day)
        sentence = requests.request('GET',"http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title="+data)
        data = data.replace("-","年",1)
        data = data.replace("-","月",1)
        a1 = data+"日"
        a2 = "农历"+today.cn_year+today.animal+"年"+today.cn_month+"月"+today.cn_day+"日"
        a3 = "干支"+today.gz_year+"年"+today.gz_month+"月"+today.gz_day+"日"
        a = a1+"    "+a2+"    "+a3
        if sentence.status_code != None:
            json1 = json.loads(sentence.text)
            b = json1['content']+"\n"+json1['note']
            pic2 = json1['picture2'].replace("\\","")
            res = requests.get(pic2)
            img = QImage.fromData(res.content)
            self.label_2.setText(a)
            self.label_3.setText(b)
            index = 0.8
            c = QPixmap.fromImage(img)
            self.label.setPixmap(c.scaled(int(float(c.width())*index),int(float(c.height())*index),aspectRatioMode=Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation))
        else:
            self.thread = msgThread(t=2)
            self.thread.finishSignal.connect(self.Change)
            self.thread.start()
            
        self.player = QMediaPlayer()
        self.player.setVolume(100)
            
    def setApis(self):
        self.dialog = Dialog()
        self.dialog.show()
        
    def Change(self, num):
        a = ""
        match num:
            case 0:
                a = "单词不能为空"
            case 1:
                a = "请检查拼写"
            case 2:
                a = "请检查网络"
        QMessageBox.warning(self, "错误", a, QMessageBox.Yes)
        self.thread.terminate()

    def search(self):
        a = self.lineEdit.text()
        if a != "":
            means = requests.get("http://fanyi.youdao.com/openapi.do?keyfrom=neverland&key=969918857&type=data&doctype=json&version=1.1&q="+a)
            if means.status_code != None:
                json2 = json.loads(means.text)
                if re.match('[^a-zA-Z]', a):
                    self.thread = msgThread(t=1)
                    self.thread.finishSignal.connect(self.Change)
                    self.thread.start()
                else:
                    if len(json2) == 5: 
                        if len(json2['basic']) == 4:
                            a = "英音：/"+json2['basic']['uk-phonetic']+"/"
                            b = "美音：/"+json2['basic']['us-phonetic']+"/"
                            self.pushButton_2.setText(a)
                            self.pushButton_2.setEnabled(True)
                            self.pushButton_3.setText(b)
                            self.pushButton_3.setEnabled(True)
                        c=json2['basic']['explains'][0].split(".",1)
                        d = c[1].split("；")
                        self.listWidget.clear()
                        self.listWidget.scrollToTop()
                        for i in range(0,len(d)):
                            a = str(i+1)+". "+str(c[0])+". "+str(d[i])
                            self.listWidget.addItem(a)  
                        if len(json2) > 3:                                  
                            self.listWidget_2.clear()
                            self.listWidget_2.scrollToTop()     
                            for i in range(0,len(json2['web'])):
                                self.listWidget_2.addItem(json2['web'][i]['key']+":")
                                for h in range(0,len(json2['web'][i]['value'])):
                                    self.listWidget_2.addItem((json2['web'][i]['value'][h]))     
                    else:
                        self.thread = msgThread(t=1)
                        self.thread.finishSignal.connect(self.Change)
                        self.thread.start()
            else:
                self.thread = msgThread(t=2)
                self.thread.finishSignal.connect(self.Change)
                self.thread.start()   
        else:
            self.thread = msgThread(t=0)
            self.thread.finishSignal.connect(self.Change)
            self.thread.start()

    def voice(self,num):
        a = ""
        match num:
            case 0:
                a = "http://dict.youdao.com/dictvoice?type=1&audio="
            case 1:
                a = "http://dict.youdao.com/dictvoice?type=0&audio="
        self.player.setMedia(QMediaContent(QUrl(a+self.lineEdit.text())))
        self.player.play()
        self.thread.terminate()

    def voice1(self):
        self.thread = voiceThread(t=0)
        self.thread.finishSignal.connect(self.voice)
        self.thread.start()

    def voice2(self):       
        self.thread = voiceThread(t=1)
        self.thread.finishSignal.connect(self.voice)
        self.thread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())