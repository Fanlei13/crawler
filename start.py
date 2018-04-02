#!/usr/bin/python
# -*-coding:utf-8-*-

import time
import os
import json
import smtplib, email

list = []

finalList = []

def deleteJson() :
    directory = "./dir"
    # os.chdir(D:\scrapy\taobao\)  # 切换到directory目录
    cwd = os.getcwd()  # 获取当前目录即dir目录下
    print cwd
    print("------------------------current working directory------------------")
    files = os.listdir(cwd)  # 列出目录下的文件
    for file in files:
        if file == 'info1.json':
            os.remove('info1.json')  # 删除文件
            print(file + ' deleted')
        if file == 'info2.json':
            os.remove('info2.json')  # 删除文件
            print(file + ' deleted')
        if file == 'info3.json':
            os.remove('info3.json')  # 删除文件
            print(file + ' deleted')
        if file == 'info4.json':
            os.remove('info4.json')  # 删除文件
            print(file + ' deleted')

    print("------------------------done------------------")


def findNotifyMe() :
    with open('D:/scrapy/tutorial/info1.json', 'r') as f:
        # print f.read()
        text = json.load(f)
        for v in text:
            if v['count'] == 1:
                list.append(v['name'])
    with open('D:/scrapy/tutorial/info2.json', 'r') as f:
        # print f.read()
        text = json.load(f)
        for v in text:
            if v['count'] == 1:
                list.append(v['name'])
    with open('D:/scrapy/tutorial/info3.json', 'r') as f:
        # print f.read()
        text = json.load(f)
        for v in text:
            if v['count'] == 1:
                list.append(v['name'])
    with open('D:/scrapy/tutorial/info4.json', 'r') as f:
        # print f.read()
        text = json.load(f)
        for v in text:
            if v['count'] == 1:
                list.append(v['name'])

    for i in range(len(list)):
        print i
        for j in range(i + 1, len(list)):
            if (list[i] == list[j] and list[i] not in finalList):
                print list[i]
                finalList.append(list[i])
                break

def sendEmail() :


    chst = email.Charset.Charset(input_charset='utf-8')

    # header里分别定义发件人,收件人以及邮件主题。
    header = ("From: %s\nTo: %s\nSubject: %s\n\n" %
              ("bvbfan@sina.com",
               "fanleiabcd@qq.com",
               chst.header_encode("mi india")))

    # 打开目标文档后读取并保存至msg这个多行str变量里。
    #f = open("./test121.txt", 'r', encoding='utf-8')
    msg = ''''''
    #msg = msg.decode('utf-8').encode('gb18030')

    for i in finalList :

        msg += i.strip() + '\n'


    # 对header和msg邮件正文进行utf-8编码，指定发信人的smtp服务器，并输入邮箱密码进行登录验证，最后发送邮件。
    email_con = header.encode('utf-8') + msg.encode('utf-8')
    smtp = smtplib.SMTP("smtp.sina.com", 25)
    smtp.login("bvbfan@sina.com", "fanlei510722")
    smtp.sendmail('bvbfan@sina.com', 'fanleiabcd@qq.com', email_con)
    smtp.quit()
    print('ok')


if __name__ == '__main__':
    print("colecting json....")
    while True:
        if time.strftime('%H:%M:%S', time.localtime(time.time())) == '06:40:00':
            os.system("scrapy crawl mi -o info1.json -t json")
            #time.sleep(14400)  #每隔一天运行一次 4*60*60=s
        if time.strftime('%H:%M:%S', time.localtime(time.time())) == '06:48:00':
            os.system("scrapy crawl mi -o info2.json -t json")
            #time.sleep(14400)  #每隔一天运行一次 24*60*60=86400s
        if time.strftime('%H:%M:%S', time.localtime(time.time())) == '06:56:00':
            os.system("scrapy crawl mi -o info3.json -t json")
            #time.sleep(14400)  #每隔一天运行一次 24*60*60=86400s
        if time.strftime('%H:%M:%S', time.localtime(time.time())) == '07:04:00':
            os.system("scrapy crawl mi -o info4.json -t json")
            #time.sleep(14400)  #每隔一天运行一次 24*60*60=86400s
        if time.strftime('%H:%M:%S', time.localtime(time.time())) == '07:12:00':
            findNotifyMe()
            sendEmail()
            deleteJson()
