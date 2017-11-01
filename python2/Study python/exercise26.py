# _*_coding:utf-8_*_

#！/usr/local/bin/python    MAC
# filename:exercise26.py

#intend :For loop  If else   while loop


def Print_For():
    listargv = ["lol","STK","Star way","only You"]
    for game in listargv:
        print game

def Print_While():
    listargv = ["zhangsan","lisi","wangwu","zhaoliu","zhouqi"]
    i = 0
    while i < 5:
        print listargv[i]
        i += 1

def Print_if():
    print """
    please input the num for you choose...
    1.For_loop.
    2.While_loop.
    """
    sure_Num = input(">")
    if sure_Num == 1:
        Print_For()
    elif sure_Num == 2:
        Print_While()

Print_if()
