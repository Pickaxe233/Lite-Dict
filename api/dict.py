import json
import requests
import re
import thread
from ui.ui_dict import Ui_MainWindow
from main import MainWindow
from PySide6.QtGui import QFontDatabase

#有道翻译
def ydtran(a=""):
    means = requests.get("http://fanyi.youdao.com/openapi.do?keyfrom=neverland&key=969918857&type=data&doctype=json&version=1.1&q="+a)
    if means.status_code != None:
        json2 = json.loads(means.text)
        if re.match('[^a-zA-Z]', a):
            threads = thread.msgThread(t=1)
            threads.finishSignal.connect(MainWindow.Change)
            threads.start()
        else:
            self.label_2.setText(a)
            self.tabWidget.setCurrentIndex(1)
            if len(json2) == 5: 
                self.textBrowser.clear()
                if len(json2['basic']) == 4:
                    id = QFontDatabase.addApplicationFont('./font/GentiumPlus-Regular.ttf')
                    name = QFontDatabase.applicationFontFamilies(id)
                    a = "BrE:/"+json2['basic']['uk-phonetic']+"/"
                    b = "AmE:/"+json2['basic']['us-phonetic']+"/"
                    self.pushButton_2.setFont(name)
                    self.pushButton_2.setText(a)
                    self.pushButton_2.setEnabled(True)
                    self.pushButton_3.setFont(name)
                    self.pushButton_3.setText(b)
                    self.pushButton_3.setEnabled(True)
                    c = json2['basic']['explains']
                    if len(c) > 1:
                        for i in range(len(c)):
                            self.textBrowser.append(c[i])
                    else:
                        self.textBrowser.append(c[0])  
            else:
                threads =  thread.msgThread(t=1)
                threads.finishSignal.connect(self.Change)
                threads.start()
    else:
        threads =  thread.msgThread(t=2)
        threads.finishSignal.connect(self.Change)
        threads.start()   
    threads = thread.msgThread(t=0)
    threads.finishSignal.connect(self.Change)
    threads.start()

#必应词典
def bing(self,a=""):