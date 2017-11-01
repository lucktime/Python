
#coding=utf-8


#https://www.mara.gov.au/api/agentsearch?DelimitedStartWithLetterFilter%5BFieldName%5D=DisplayBusiness.Name&DelimitedStartWithLetterFilter%5BLetterString%5D=&DelimitedStartWithLetterFilter%5BLabel%5D=Show+All&DelimitedStartWithLetterFilter%5BIsSelected%5D=false&DelimitedStartWithLetterFilter%5BContainsData%5D=true&Keyword=&Location=melbo&BusinessName=&IsNoFee=&IsPractitioner=&AgentFamilyName=&AgentGivenName=&AgentName=&AgentMARN=&SortInfo%5BSortField%5D=&SortInfo%5BIsAscending%5D=false&PagingInfo%5BPageIndex%5D=0&PagingInfo%5BPageSize%5D=20

from selenium import webdriver
# get encode uncode by base64
import base64

# get xpath by BeautifulSoup  == make base sdk
from bs4 import BeautifulSoup

import time
# get get time by sleep  eg:time.sleep(0.1)
from time import sleep

import random
# get re way   eg:match = re.search(r'[\w.-]+@[\w.-]+', Fi_Email)
import re
import csv
import unicodecsv
#import unicodecsv               ========make
from cStringIO import StringIO
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import json

import urllib2

from lxml import etree

#step:(1) ----
pageIndex = 16
arrayHref = []
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)

driver.set_window_size(1120, 550)
while (pageIndex < 65):
   pageIndex = pageIndex + 1
   strPageIndex = str(pageIndex)
   link = 'https://www.mara.gov.au/api/agentsearch?DelimitedStartWithLetterFilter%5BFieldName%5D=DisplayBusiness.Name&DelimitedStartWithLetterFilter%5BLetterString%5D=&DelimitedStartWithLetterFilter%5BLabel%5D=Show+All&DelimitedStartWithLetterFilter%5BIsSelected%5D=false&DelimitedStartWithLetterFilter%5BContainsData%5D=true&Keyword=&Location=melbo&BusinessName=&IsNoFee=&IsPractitioner=&AgentFamilyName=&AgentGivenName=&AgentName=&AgentMARN=&SortInfo%5BSortField%5D=&SortInfo%5BIsAscending%5D=false&PagingInfo%5BPageIndex%5D=' + strPageIndex + '&PagingInfo%5BPageSize%5D=20'
  # link = 'https://www.mara.gov.au/api/agentsearch?DelimitedStartWithLetterFilter%5BFieldName%5D=DisplayBusiness.Name&DelimitedStartWithLetterFilter%5BLetterString%5D=&DelimitedStartWithLetterFilter%5BLabel%5D=Show+All&DelimitedStartWithLetterFilter%5BIsSelected%5D=false&DelimitedStartWithLetterFilter%5BContainsData%5D=true&Keyword=&Location=Sydney&BusinessName=&IsNoFee=&IsPractitioner=&AgentFamilyName=&AgentGivenName=&AgentName=&AgentMARN=&SortInfo%5BSortField%5D=&SortInfo%5BIsAscending%5D=false&PagingInfo%5BPageIndex%5D=' + strPageIndex + '&PagingInfo%5BPageSize%5D=20'
   print pageIndex
   # input csv file
   csvPageindexfile = file('hrefFile-melbou1.csv', 'a+')
   writer = unicodecsv.writer(csvPageindexfile,encoding='utf-8')
    #writer.writerow(['name', 'class', 'type','Address','Po_Address','Phone','Fax','Ma_Office','email'])
   hrefdb = (pageIndex,link)
   hrefdata = [
      hrefdb
        ]
   writer.writerows(hrefdata)
   csvPageindexfile.close()

   #read anyever href，get json
   response = urllib2.urlopen(link)
   html = response.read()
   #print html
   #break
   data = json.loads(html)
   busness = data["Result"]
   postal_add_Data = ""
   for bus in busness :
       dataID = bus['ContactId']
       #print data
       dataID = 'https://www.mara.gov.au/search-the-register-of-migration-agents/registered-migration-agent-details/?id='+ dataID
       #arrayHref.append(dataID)
       print dataID
       #取出一条数据
    #   break
   #break
#print arrayHref

#step:(2) ----


       driver.get(dataID)
       sub_html = BeautifulSoup(driver.page_source, "lxml")

    #print sub_html
    #===============AnyDom bus Details
       d_d = sub_html.find("div",{"id":"agentDetail"})
    #=============== Bus Name
       d_d_contai = d_d.find("div",{"class":"agentHeadingContainer"})
    #====get People name
       name = d_d_contai.h3.span.get_text().strip().encode('utf-8')
       d_d_name = d_d_contai.findAll("span")
       name = d_d_name[0].text +  d_d_name[1].text +  d_d_name[2].text
       #print d_d_name
    #for spran in d_d_name :
       print name


    #get Email address,
    #Postal address
       d_d_bigSe = d_d.find("div",{"class":"bigSection"})
       d_d_Data = d_d_bigSe.findAll("span")
    #====get People email
       if len(d_d_Data) >= 2:
           email_add_data =  d_d_Data[1].text.strip().encode('utf-8')
           email_add_data = email_add_data.replace(':','')

    #====get People Postal
       if len(d_d_Data) >= 4:
           postal_add_Data = d_d_Data[3].text.strip().encode('utf-8')
           print email_add_data
           print postal_add_Data
    #break;

	#get Business name, Phone,Fax,Business Address,Relation to business
       d_d = sub_html.find("div",{"id":"agentDetail"})
    #=============== Bus get Email
       d_d_busSetion = d_d.find("div",{"class":"smallSection businessSection"})
       d_d_BusDate = d_d_busSetion.findAll("span")
    #print d_d_BusDate

    #====get business Name
       if len(d_d_BusDate) >= 2:
          bus_Name_data =  d_d_BusDate[1].text.strip().encode('utf-8')
          if len(d_d_BusDate) >= 4:
    #====get business Phone
             bus_Phone_data = d_d_BusDate[3].text.strip().encode('utf-8')
    #====get business Fax
             if len(d_d_BusDate) >= 6:
                bus_Fax_data = d_d_BusDate[5].text.strip().encode('utf-8')
    #====get business Add
                if len(d_d_BusDate) >= 8:
                   bus_Add_data = d_d_BusDate[7].text.strip().encode('utf-8')
       print bus_Name_data
       print bus_Phone_data
       print bus_Fax_data
       print bus_Add_data


    #break;
# input csv file
       csvfile = file('csvtest-melbouplus.csv', 'a+')
       writer = unicodecsv.writer(csvfile,encoding='utf-8')
    #writer.writerow(['name', 'class', 'type','Address','Po_Address','Phone','Fax','Ma_Office','email'])
       db = (name,email_add_data, postal_add_Data, bus_Name_data, bus_Phone_data, bus_Fax_data, bus_Add_data,dataID)
       data = [
        db
        ]
       writer.writerows(data)
       csvfile.close()

       time.sleep(3)
