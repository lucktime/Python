# _*_coding:utf-8_*_

#！/usr/local/bin/python    MAC
# filename:exercise15.py

#intend :Prompting And Open the file

from sys import argv
# import os
from os.path import exists


listargv = []
prompting = ">"
listargv.append(raw_input("please input packname:\n" + prompting))
listargv.append(raw_input("please input The txt filename:\n" + prompting))

filename = listargv[1]
if exists(filename):
    message = 'OK, the "%s" file exists.'
    print message % filename
else:
    message = "Sorry, I cannot find the '%s' file.Creat File "
    txt = open(filename,'w')
    txt.write(raw_input(message % filename +"\n" + prompting + "input the file:"))
    # print message % filename


# txt.truncate()
packname,filename = listargv
# f=open('f.txt','w')
txt = open(filename)

print "are you sure the name is %s" %filename
sure = raw_input(prompting + "Y/N:")
if sure == "Y":
    print txt.read()
    txt.close()
else:
    print "error,not file open this"
