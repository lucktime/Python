#_*_coding:utf8_*_
#！/usr/local/bin/python    MAC
# Filename: Spider_poi.py
#intend: name,lat,lng,address,telephone


from selenium import webdriver
from bs4 import BeautifulSoup
import urllib2
import urllib
import re
import csv
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
#     "(KHTML, like Gecko) Chrome/15.0.87"
# )
# driver = webdriver.PhantomJS(desired_capabilities=dcap)
userAgent = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)
headers = {'User-Agent':userAgent}
# get href content

# step 1 get all class
try:
    # file = open('.\\Class.txt','a')
    # classarray = ['美食','宾馆','购物','汽车服务','生活服务','结婚','丽人','金融','休闲娱乐','运动健身','医疗','旅游景点','教育','培训机构','房地产','自然地物','行政区划','政府机构','公司企业',
    # '门址道路','交通线']
    classarray = ['行政区划','政府机构','公司企业',
    '门址道路','交通线']
    i = 1
    nestclass = 0
    for i in range(1,252):
        url = "http://api.map.baidu.com/place/v2/search?query="+classarray[nestclass]+"&page_size=10&page_num="+ str(i*1) +"&scope=1&region=桂林&output=json&ak=aIxuXK73RFaXDjUysrflBEaod6o92KGD"
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile(r'"name":"([\d\D]*?)",[\d\D]*?"lat":([\d\D]*?),[\d\D]*?"lng":([\d\D]*?)},[\d\D]*?"address":([\d\D]*?),[\d\D]*?"telephone":"([\d\D]*?)"')
        items = re.findall(pattern,content)
        # if (len(items) <0):
        #     continue;
        for item in items:
            print "name:",item[0]
            print "lat:",item[1]
            print "lng:",item[2]
            print "address:",item[3]
            print "telephone:",item[4]
            print "===="+classarray[nestclass]+"====  "+str(i*1)+"  ========="
            # savestr = str(item[0])+ ';'+str(item[1])+ ';'+str(item[2])+ ';'
            filename = classarray[nestclass];
            csvfile = file(filename+'.csv', 'a+')
            writer = csv.writer(csvfile)
            #writer.writerow(['name', 'lat', 'lng','address','telephone'])
            data = [
            (item[0], item[1], item[2], item[3], item[4])
            ]
            writer.writerows(data)
            csvfile.close()

except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason
finally:
    pass
