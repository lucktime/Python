
#coding=utf-8

import time
from selenium import webdriver
import base64
from bs4 import BeautifulSoup
from time import sleep
import re

import urllib2

import numpy
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


link = 'http://www.lawsociety.com.au/community/findingalawyer/findalawyersearch/FirmResultList/index.htm?Region3=0&firmname=&FirmNameMatchType=Starts&firm_type=Any&limit_search=&Suburb3=sydney'

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)
# get href content
content = urllib2.urlopen(link).read()


driver.set_window_size(1024, 550)

driver.get(link)
# sub_html = BeautifulSoup(driver.page_source, "lxml")
s = BeautifulSoup(content,"html5lib")

# print s
#r = re.compile(r'jobdetail\.ftl\?job=\d+$')
# Alltr = s.findAll("tr")
# print Alltr[356]
#ok
tdata = s.find("div", {"id": "resultTable"})
# print tdata
# print tdata
print "================"
data_a = tdata.findAll("a",href=True)
print len(data_a)
# print data_a[0]
i = 0
while(i<len(data_a)):
    href = data_a[i*2]["href"]
    i += 1
    print i
    sub_link = "http://www.lawsociety.com.au" +  href        #ok
    print sub_link
# input csv file

    print "================"
    driver.get(sub_link)
    sub_html = BeautifulSoup(driver.page_source, "lxml")

    d_d = sub_html.find("div",{"id":"col1"})
    d_d_tr = d_d.findAll("tr")


    name = ""
    Class = ""
    Type = ""
    Address = ""
    Po_Address = ""
    Phone = ""
    Fax = ""
    Ma_Office = ""
    Fi_Email = ""
    for tr in d_d_tr:
        td = tr.findAll("td")
        print "==!!! tr====="
        # INPUT class.name two mothod

        #print td[0].text
        print "----"
        #print td[1].text
        print "----"

        if td[0].text == 'Name' :
            #global name
            name = td[1].text.strip().encode('utf-8')
        if td[0].text == 'Class' :
            #global Class
            Class = td[1].text.strip().encode('utf-8')
        if td[0].text == 'Type' :
            #global Type
            Type = td[1].text.strip().encode('utf-8')
        if td[0].text == 'Address' :
            #global Address
            Address = td[1].text.strip().encode('utf-8')
        if td[0].text == 'Postal Address' :
            #global Po_Address
            Po_Address = td[1].text.strip().encode('utf-8')
        if td[0].text == 'Phone' :
            #global Phone
            Phone = td[1].text.strip().encode('utf-8')
        if td[0].text == 'Fax' :
            #global Fax
            Fax = td[1].text.strip().encode('utf-8')
        if td[0].text == 'Main Office' :
            #global Ma_Office
            Ma_Office = td[1].text.strip().encode('utf-8')
        if td[0].text == 'Firm Email' :
            #global Ma_Office
            Fi_Email = td[1].text.strip().encode('utf-8')
            emails =  Fi_Email.find("@")
            if emails > 0 :
                #print "!!!!!!!!"
                match = re.search(r'[\w.-]+@[\w.-]+', Fi_Email)
                if match:
                    email =  match.group()
                    Fi_Email = email.strip().encode('utf-8')
                    break



    #完成一个公司
        # _*_ coding:utf-8 _*_
        #xiaohei.python.seo.call.me:)
        #win+python2.7.x
    import csv
    csvfile = file('lawsocietyv1.0.csv', 'a+')
    writer = csv.writer(csvfile)
    #writer.writerow(['name', 'class', 'type','Address','Po_Address','Phone','Fax','Ma_Office','email'])
    data = [
    (name, Class, Type,Address,Po_Address,Phone,Fax,Ma_Office,Fi_Email)
    ]
    writer.writerows(data)
    csvfile.close()




#ok
#pages = s.find("ul", {"id": "theTable-tablePaginater"})
#print pages;



#http://www.crifan.com/unicodeencodeerror_gbk_codec_can_not_encode_character_in_position_illegal_multibyte_sequence/
"git scrpts"
