from dataclasses import replace
import json
import requests
import datetime
import webbrowser
import argparse
import playsound
import time
from borax.calendars.lunardate import LunarDate

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="查询英语单词释义")
    parser.add_argument("word", help="输入要查询的单词",type = str)
    #parser.add_argument("--settings",'-s',type = str,choices = ["picture","sentence","date","lunar-date"],help='设置')
    parser.add_argument('--version', '-v', action='version',version='版本:A01', help='显示版本')
    args = parser.parse_args()

    date = datetime.date.today()
    data = str(date)
    today = LunarDate.from_solar_date(date.year,date.month,date.day)
    sentence = requests.request('GET',"http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title="+data)
    json1 = json.loads(sentence.text)
    print("今天是",date.year,"年",date.month,"月",date.day,"日, 农历",today.cn_year+today.animal,"年"+today.cn_month+"月"+today.cn_day+"日")
    print("\n每日一句：")
    print(json1['content']+"\n"+json1['note']+"\n")
    pic2 = json1['picture2'].replace("\\","")
    #webbrowser.open(pic2, new=2, autoraise=True)

    means = requests.get("http://fanyi.youdao.com/openapi.do?keyfrom=neverland&key=969918857&type=data&doctype=json&version=1.1&q="+args.word)
    json2 = json.loads(means.text)
    print("英音："+json2['basic']['uk-phonetic'],"美音："+json2['basic']['us-phonetic'])
    #playsound.playsound("http://dict.youdao.com/dictvoice?type=1&audio="+args.word)
    #playsound.playsound("http://dict.youdao.com/dictvoice?type=0&audio="+args.word)
    print(json2['basic']['explains'][0])
    print("\n网络释义：")
    for i in range(0,len(json2['web'])):
        print(json2['web'][i]['key']+"：")
        for h in range(0,len(json2['web'][i]['value'])):
            print(json2['web'][i]['value'][h])