#_*_coding:utf8_*_
#！/usr/local/bin/python    MAC
# Filename: Spider_poi.py
#intend: image,title,price,class


from selenium import webdriver
from bs4 import BeautifulSoup
import urllib2
import urllib
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)
# get href content

# link = 'https://www.hardtofind.com.au/'
# # ok  get All root  href
# content = urllib2.urlopen(link).read()

# driver.get(link) //因为你，卡了很久不出现结果，一会谷歌，查看原因
# s = BeautifulSoup(content,"html5lib")
# nav_Data = s.find("div", {"id": "primary-nav-control"})
# roothref_data = nav_Data.find("ul", {"class": "menu ie8-menu "})
# rootli_Arr = roothref_data.findAll("li")
# roothref_Arr = nav_Data.findAll("a", href=True)


# step 1 get all class
hrefarray = ['gifts','home-garden','prints-art','fashion','jewellery','men','kids','weddings']
for href in hrefarray:
    page = -1;
    while (page < 200):
        page = page + 1
        strPageIndex = str(page)
        href_a = "https://www.hardtofind.com.au/categories/"+href+"?page="+strPageIndex
        print "======"+strPageIndex+"==="+href
        content = urllib2.urlopen(href_a).read()
        s = BeautifulSoup(content,"html5lib")
        nav_Data = s.find("div", {"id": "products"})
        roothref_data = nav_Data.findAll("div", {"class": "sale-item-text-wrap"})
        index = 0
        maxindex = len(roothref_data) - 1

        for webhref in roothref_data:
            if (index >= maxindex):
                break
            index = index + 1
            lablehref = webhref.find("a",href=True)
            page_href =  lablehref["href"]
            threecontent = urllib2.urlopen(page_href).read()
            s = BeautifulSoup(threecontent,"html5lib")
            page_form = s.find("form",{"id":"form_add_to_cart"})
            page_title = page_form.find("div",{"class":"title"})
            title = page_title.h1.string
            print title
#            price = page_title.find("span",{"class":"price price-discount"}).string
#            print price
            page_image =s.find("div",{"class":"galleryContainer"})
#            image = page_image.findAll("a")
#            print image
#            print image
            page_class = s.find("div",{"class":"pagination"})
            classname = page_class.get_text().strip().encode('utf-8')
            classname = classname.replace(' ', '').replace('\n','>')
            print classname






    # pass
