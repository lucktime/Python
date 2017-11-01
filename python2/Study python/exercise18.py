# _*_coding:utf-8_*_

#！/usr/local/bin/python    MAC
# filename:exercise18.py

#intend :what is def.and method


def plus(arg1,arg2):
    arg3 = arg1 + arg2
    print " %d + %d = %d" %(arg1 ,arg2 ,arg3)

def minux(arg1, arg2):
    arg3 = arg1 - arg2
    print " %d - %d = %d" %(arg1 ,arg2 ,arg3)

def asterisk(arg1, arg2):
    arg3 = arg1 * arg2
    print " %d * %d = %d" %(arg1 ,arg2 ,arg3)

def slash(arg1, arg2):
    arg3 = arg1 / arg2
    print " %d / %d = %d" %(arg1 ,arg2 ,arg3)

def print_int(arg):
    print "You cloose %r." %arg
# def slash(arg1):
#     print "Slash Only one variables "  error
print "1:say hello"
print "2:say Goodbye"
print "3:say GG"

num_input = raw_input(">" )
print num_input
if num_input == "1":
    print_int(num_input)
elif num_input == "2":
    print_int(num_input)
elif num_input == "3":
    print_int(num_input)
else:
    print_int(num_input)

plus(2,3)

minux(3,2)

asterisk(3,5)

slash(8,2)
