# python2和python3对比学习以及知识点的总结
### 1.print 区别
python2 结果
```
**** 区别1 print的结果
##支持python2 和 支持 python3
print("hello world")
print("i'm the library")
print("i'm so happy for the world")
##以下部分不支持python3

print "good"
print "Hello again"
print "I like taping this"
print "Yes! Printing"


# 在 python2 会输出结果   ('3 plus 4 equla =', 7)
# 咋 python3 会输出结果   3 plus 4 equla = 7
print ("3 plus 4 equla =",3+4)

# 在 python2 会输出结果  3 plus 4 equla =  7
# 咋 python3 会报错
print "3 plus 4 equla = ", 3+4

**** 区别2 对于float 浮点数的处理结果

代码：
print ("7.0 / 3.0 equla =",7.0/3.0)
print ("7 / 3 equla =",7/3)
# python3 处理浮点时
7.0 / 3.0 equla = 2.3333333333333335
7 / 3 equla = 2.3333333333333335
# python2 处理浮点时
'7.0 / 3.0 equla =', 2.3333333333333335
'7 / 3 equla =', 2

**** 区别3 字符串的拼接
代码：
end1 = 'h'
end2 = 'o'
end3 = 'b'
end4 = 'b'
end5 = 'y'
end6 = 'R'
end7 = 'U'
end8 = 'N'
print (end1+end2+end3+end4+end5),
print (end6+end7+end8)
# python2 会显示结果 python2 会拼接字符串
hobby RUN
# python3 会显示结果，python3 会自动换行
hobby
RUN
解决办法：
print (end1+end2+end3+end4+end5,end=" ") 即可
```

### 2.ASCll编码的问题
由于在国外，文本编辑器的编码不一致。而造成的错误，所以建议在py脚本的头部添加 # -*- coding:utf-8 -*-  
这样脚本就会执行 Unicode utf-8 编码了，从而不会造成关于ASCLL编码不同意的问题啦。
对于# -*- coding:utf-8 -*-，python是忽略的。但它却是编程人员定制文件格式的一种方式 

### 3.使用两种方式输出 一种采用占位符，一种用逗号.(被称为格式化字符串)
```
print ("my name is %s i'm age is %s my sex is %s my height is %s my hobby is %s" %(name ,age ,sex ,height, hobby))
print ('my name is',name,'i\'m age is',age,'my sex is',sex,'my height is',height,'my hobby is',hobby)
```

有%s ,%r ,%d
%r用rper()方法处理对象
%s用str()方法处理对象
%d用来处理数字

```
eg：例如：
[python] view plain copy
text = "I am %d years old." % 22  
print "I said: %s." % text  
print "I said: %r." % text  
返回结果：
[python] view plain copy
I said: I am 22 years old..  
I said: 'I am 22 years old.'. // %r 给字符串加了单引号 

eg2: 例如：
import datetime  
d = datetime.date.today()  
print "%s" % d  
print "%r" % d  

返回结果：
[python] view plain copy
2014-04-14  
datetime.date(2014, 4, 14)  
```

### raw_input() 和 input()
1、在python2.x中raw_input( )和input( )，两个函数都存在，其中区别为
raw_input( )---将所有输入作为字符串看待，返回字符串类型
input( )-----只能接收“数字”的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）

2、在python3.x中raw_input( )和input( )进行了整合，去除了raw_input( )，仅保留了input( )函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
### 本地查看python2和python3 的pydoc的文档
可以执行 python3 -m pydoc -p 3333 任意端口号
或者    python  -m pydoc -p 3333 任意端口号