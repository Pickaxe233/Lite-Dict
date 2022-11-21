import json
import requests
import datetime
from borax.calendars.lunardate import LunarDate
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
import dict
import keyboard
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl
import re
import time

date = datetime.date.today()
data = str(date)
today = LunarDate.from_solar_date(date.year,date.month,date.day)
sentence = requests.request('GET',"http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title="+data)
json1 = json.loads(sentence.text)
data = data.replace("-","年",1)
data = data.replace("-","月",1)
a1 = data+"日"
a2 = "农历"+today.cn_year+today.animal+"年"+today.cn_month+"月"+today.cn_day+"日"
a3 = "干支"+today.gz_year+"年"+today.gz_month+"月"+today.gz_day+"日"
a = a1+"    "+a2+"    "+a3
b = json1['content']+"\n"+json1['note']
pic2 = json1['picture2'].replace("\\","")
res = requests.get(pic2)
img = QImage.fromData(res.content)

def word_error(b = 0, a = ""):
    match b:
        case 0:
            a = "单词不能为空"
        case 1:
            a = "请检查拼写"
    QMessageBox.critical(MainWindow, "错误", a, QMessageBox.Yes)

def day():
    ui.label_2.setText(a)
    ui.label_3.setText(b)
    index = 0.8
    c = QPixmap.fromImage(img)
    ui.label.setPixmap(c.scaled(int(float(c.width())*index),int(float(c.height())*index),aspectRatioMode=Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation))

def search():
    a = ui.lineEdit.text()
    if a != "":
        means = requests.get("http://fanyi.youdao.com/openapi.do?keyfrom=neverland&key=969918857&type=data&doctype=json&version=1.1&q="+a)
        json2 = json.loads(means.text)
        if re.match('[^a-zA-Z]', a):
            word_error(1)
        else:
            if len(json2) == 5: 
                if len(json2['basic']) == 4:
                    a = "英音：/"+json2['basic']['uk-phonetic']+"/"
                    b = "美音：/"+json2['basic']['us-phonetic']+"/"
                    ui.pushButton_2.setText(a)
                    ui.pushButton_2.setEnabled(True)
                    ui.pushButton_3.setText(b)
                    ui.pushButton_3.setEnabled(True)
                c=json2['basic']['explains'][0].split(".",1)
                d = c[1].split("；")
                ui.listWidget.clear()
                ui.listWidget.scrollToTop()
                for i in range(0,len(d)):
                    a = str(i+1)+". "+str(c[0])+". "+str(d[i])
                    ui.listWidget.addItem(a)  
                if len(json2) > 3:                                  
                    ui.listWidget_2.clear()
                    ui.listWidget_2.scrollToTop()     
                    for i in range(0,len(json2['web'])):
                        ui.listWidget_2.addItem(json2['web'][i]['key']+":")
                        for h in range(0,len(json2['web'][i]['value'])):
                            ui.listWidget_2.addItem((json2['web'][i]['value'][h]))     
            else:
                word_error(1)
    else:
        word_error(0)

def voice1():
    player = QMediaPlayer()
    player.setVolume(100)
    a = ui.lineEdit.text()
    player.setMedia(QMediaContent(QUrl("http://dict.youdao.com/dictvoice?type=1&audio="+a)))
    player.play()
    time.sleep(player.duration()+2)

def voice2():
    player  = QMediaPlayer()
    player.setVolume(100)    
    player.setMedia(QMediaContent(QUrl("http://dict.youdao.com/dictvoice?type=0&audio="+a)))
    player.play()
    time.sleep(player.duration()+2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = dict.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(search)
    ui.pushButton_2.clicked.connect(voice1)
    ui.pushButton_3.clicked.connect(voice2)
    day()
    keyboard.add_hotkey("enter",search)
    sys.exit(app.exec_())