#_*_coding:utf8_*_
#！/usr/local/bin/python    MAC
# Filename: net114_Aozhou.py

#intend : craw corp.net114.com  about Aozhou  info

#html http://corp.net114.com/scat-aozhou.html

import time
from selenium import webdriver
import base64
from bs4 import BeautifulSoup
from time import sleep
import re

import csv
import urllib2
import codecs
import unicodecsv
import numpy
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)
# get href content
page = 17
while page < 100:
    print page , "=================="
    strPage = str(page)
    link = 'http://corp.net114.com/scat-aozhou-p-%s.html' %strPage    # ok  get All root  href
    content = urllib2.urlopen(link).read()


    driver.set_window_size(1024, 550)

    driver.get(link)
    s = BeautifulSoup(content,"html5lib")

    tdata = s.find("div", {"id": "corp_left_content"})
    LeftData = tdata.findAll("div", {"class": "left w_427 border_left_right"})

    for data in LeftData:
        data_a = data.findAll("a",href=True)
        for href in data_a:
            WebHref =  href["href"]   # OK Get href
            driver.get(WebHref)
            WebHtml = BeautifulSoup(driver.page_source, "lxml")

            if "gongsi" in WebHref:
                has_Type = False
            else:
                has_Type = True

            if has_Type == True:
                if WebHtml.find("div",{"class":"sorry"}):
                    break
                d_d = WebHtml.find("div",{"class":"bg_white p_7"})

                d_info = d_d.find("div",{"class":"div_text"})
            # print d_info.find_all('p')
                d_ddata = d_info.find_all('p')
            # StringDom = "("
                csvfile = file('net114v1.0.csv', 'a+')
                writer = unicodecsv.writer(csvfile,encoding='utf-8')
                csvfile.write(codecs.BOM_UTF8)
                writer = csv.writer(csvfile)
                if len(d_ddata) >= 1:
                    name = d_ddata[0].string
                    print name
                if len(d_ddata) >= 2:
                    phonenum = d_ddata[1].string
                    print phonenum
                if len(d_ddata) >= 3:
                    address = d_ddata[2].string
                    print address
                #address = u'address
                #address.decode('gbk','ignore').encode('utf-8')
                 #以gbk编码读取（当然是读取gbk编码格式的文字了）并忽略错误的编码，转换成utf-8编码输出
                if len(d_ddata) >= 4:
                    web = d_ddata[3].string
                    print web
                if len(d_ddata) >= 5:
                    other1 = d_ddata[4].string.encode('utf-8')
                    print other1
                if len(d_ddata) >= 6:
                    other2 = d_ddata[5].string.encode('utf-8')
                    print other2

                db = (name,phonenum, address, web, other1, other2)
                data = [
                db
                ]
                writer.writerows(data)
                csvfile.close()
                break
            elif has_Type == False:
                if WebHtml.find("div",{"class":"sorry"}):
                    break
                d_d = WebHtml.find("div",{"class":"right w_453 enterprise_details"})
                #d_info = d_d.find("div",{"class":"div_text"})
                # print d_info.find_all('p')
                d_ddata = d_d.find_all('p')
                print len(d_ddata)
                            # StringDom = "("
                csvfile = file('net114v1.0.csv', 'a+')
                writer = unicodecsv.writer(csvfile,encoding='utf-8')
                csvfile.write(codecs.BOM_UTF8)
                writer = csv.writer(csvfile)
                other5 =  ""
                other6 =  ""
                other7 =  ""
                other8 =  ""
                other1 =  ""
                other2 =  ""
                other3 =  ""
                other4 =  ""
                if len(d_ddata) >= 1:
                    name = d_ddata[0].text.encode('utf-8')
                    print name
                if len(d_ddata) >= 2:
                    phonenum = d_ddata[1].text.encode('utf-8')
                    print phonenum
                if len(d_ddata) >= 3:
                    address = d_ddata[2].text.encode('utf-8')
                    print address
                if len(d_ddata) >= 4:
                    web = d_ddata[3].text.encode('utf-8')
                    print web
                if len(d_ddata) >= 5:
                    other1 = d_ddata[4].text.encode('utf-8')
                    print other1
                if len(d_ddata) >= 6:
                    other2 = d_ddata[5].text.encode('utf-8')
                    print other2
                if len(d_ddata) >= 7:
                    other3 = d_ddata[6].text
                    print other3
                if len(d_ddata) >= 8:
                    other4 = d_ddata[7].text.encode('utf-8')
                    print other4
                if len(d_ddata) >= 9:
                    other5 = d_ddata[8].text.encode('utf-8')
                    print other5
                if len(d_ddata) >= 10:
                    other6 = d_ddata[9].text.encode('utf-8')
                    print other6
                if len(d_ddata) >= 11:
                    other7 = d_ddata[10].text.encode('utf-8')
                    print other7
                if len(d_ddata) >= 12:
                    other8 = d_ddata[11].text.encode('utf-8')
                    print other8

                db = (name,phonenum, address, web, other1, other2,other3,other4,other5,other6,other7,other8)
                data = [
                db
                ]
                writer.writerows(data)
                csvfile.close()
                break
            break


    page += 1
    time.sleep(3)
# while(i<len(LeftData)):
#     data_a = LeftData[0].findAll("a",href=True)
    # href = data_a[i]["href"]
#     i += 1
#     print href
#     sub_link = href
