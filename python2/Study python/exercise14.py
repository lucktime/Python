# _*_coding:utf-8_*_

#！/usr/local/bin/python    MAC
# filename:exercise14.py

#intend :Prompting And Passing

from sys import argv

listargv = []
listargv.append(raw_input("please Input unpacking Name:"))
listargv.append(raw_input("please Input user_Name:"))

script,user_Name = listargv

prompting = ">"
print "the unpacking Name:",script
print "the user_Name is :",user_Name

print "Are you OK?"
sure = raw_input(prompting)

print "%s is your Name ?" %user_Name
sure_Yourname = raw_input(prompting)

print "Do you like China,And Where are From?"
sure_likeChina = raw_input(prompting + "Yes/No？")
sure_whereFrom = raw_input(prompting + "From：")


print "i'm %s,my name %s is %s. i %s like China,And i from %s" %(sure,sure_Yourname,user_Name,sure_likeChina,sure_whereFrom)
