# _*_coding:utf-8_*_

#！/usr/local/bin/python    MAC
# filename:exercise13.py

#intend :unpacking,Variables,Parameters

from sys import argv

listargv = []
listargv.append(raw_input("plesase Input packing Name:"))
listargv.append(raw_input("plesase Input first variables:"))
listargv.append(raw_input("plesase Input second variables:"))
listargv.append(raw_input("plesase Input third variables:"))
script,first,second,third = listargv
print "The script Is Called:",script
print "The First variables Is ",first
print "The Second variables IS ",second
print "The Third variables Is",third
