# _*_ coding:utf8 _*_

#！/usr/local/bin/python    MAC
# Filename: exercise4.py
# intend :variables And Names
# intend :More variables And Printing
# intend :String And text
# intend :More Printing
# intend ：Printing Printing

base_num = 10.0
plusnum = base_num + 10
minux_num = base_num - 8.2
asterisk_num = base_num * 2

string1 = "1234rewq"
string2 = 'qwert0988'
string3 = "1234rew"

print "10.0 + 10 = %f" % plusnum
print "10.0 - 8.2 = %f" % minux_num
print "10.0 * 2 = %f" % asterisk_num
print "plus_num * minux_num = %f" %(plusnum * minux_num)

print string1 * 2
print string1 + string2
#print string1 - string3      #    error edit


#more Printing
print '*' * 10
print 'good %s' %'second'
print string1 + string2,
print string3

#printing pringting

tube = "%r %r %r %r"
print tube % (1,2,3,4)
print tube % ("a","b","c","d")
print tube % (True,False,False,True)
print tube % (
"i'm ok",
"are you ok",
"from Leijun",
"Good fine"
)
print tube % (tube,tube,tube,tube)
