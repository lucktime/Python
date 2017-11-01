# -*- coding:utf-8 -*-
#intend:Raw_input use Way

'''
1、在python2.x中raw_input( )和input( )，两个函数都存在，其中区别为
raw_input( )---将所有输入作为字符串看待，返回字符串类型
input( )-----只能接收“数字”的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）

2、在python3.x中raw_input( )和input( )进行了整合，去除了raw_input( )，仅保留了input( )函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
'''
print ("What is your name?",end=" "),
name = input()
print ("my name is %r" %name)
print ("What is age ?",end=" "),
age = input()
print ("my age is %r" %age)

# or secord way
name = input("What is you name?")
print ("my name is %r" %name)

age = input("What is you age?")
print ("my age is %r" %age)

