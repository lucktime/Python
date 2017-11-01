#coding:UTF-8
from qqbot import _bot as bot
from threading import Timer
import time
#  Python 内置的模块，它是一个调度（延时处理机制）
import sched

from utils.const_value import QQQUANAPI

from urllib import request, parse
import json
import requests

# 1.0 版本 能够向用户和群发送消息。  ok
'''
插件 qqbot
'''
# 1.0.1版本 能够定时循环 向群和用户发送消息。ok
'''
库 
time 定时器
sched 调度延时处理机制
'''
# 1.0.2版本 能够取api的数据，向群和用户发送消息。实现python的api调用
def sendMsgToGroup(msg,groupList,bot):
    for group in groupList:
        bg=bot.List('group', group)
        if bg is not None:
            bot.SendTo(bg[0],msg)

def sendMsgToBuddy(msg,buddyList,bot):
    for buddy in buddyList:
        bg=bot.List('buddy', buddy)
        if bg is not None:
            bot.SendTo(bg[0],msg)
        pass

schedule = sched.scheduler(time.time, time.sleep)
# 设置定时循环任务，循环执行事件 被周期性调度触发的函数
def setTaskTime(inc):
    schedule.enter(inc, 0, setTaskTime, (inc,))

    #定时发送消息到qq群
    sendMessageToQQ()

def sendMessageToQQ():
    groupMsg='123'
    buddyMsg='123'
    with open('./qq.txt','r') as fr:
        qqGroup=fr.readline().strip()
        qqBuddy=fr.readline().strip()
    qqGroupList=qqGroup.split(',')
    qqBuddyList=qqBuddy.split(',')
    sendMsgToGroup(groupMsg,qqGroupList,bot)
    sendMsgToBuddy(buddyMsg,qqBuddyList,bot)


def sendQQquanMessageToQQ(goods):
 
    for good in goods:
        with open('./test.txt', 'wt') as f:
            print(good, file=f)
            # return good
            groupMsg = json.dumps(good)
            buddyMsg = json.dumps(good)
            print (buddyMsg.encode("UTF-8"))
            return 
    
def onQQMessage(bot, contact, member, content):
    if bot.isMe(contact, member):
        print('This is me')

# 通过qq券api，获取到数组数据。
def sendQQQuanApi():
    try:
        # step1：调用接口，获取数据。
        result = requests.get(QQQUANAPI, params={
        }, timeout=1)
        # 格式化数据
        # result = result.encode("UTF-8")
        date = json.loads(result.text.encode("UTF-8"))
        # step2:取出数据数组结果格式化代码，并取出想要的数组。
        goods = date['data']['result']
        return goods
        # 写入到数据库中
    except Exception:
        print('网络错误处理')
    
def main(bot,inc=60):
    #获取数组数据 
    # goods = sendQQQuanApi()
    # #将数组传递给 sendQQquanMessageToQQ
    # sendQQquanMessageToQQ(goods)

    # print(result.text)
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    schedule.enter(0, 0, setTaskTime, (inc,))
    schedule.run()

if __name__=='__main__':
    bot.Login(['-q', '757534571'])
    main(bot,10)
