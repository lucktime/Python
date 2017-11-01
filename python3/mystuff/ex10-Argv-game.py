# -*- coding:utf-8 -*-
#intend:try to complete the game

from sys import argv

# unpack the argv python 后面必须传递两个参数 ，第一个参数是文件名，第二个参数 是游戏名 eg:python3 ex10-Argv-game.py music or python3 ex10-Argv-game.py play
filename,gamename = argv
if gamename == 'music':
    print ('we can play the music')
    music = input("What do you like the music?")
    print("i like %r" %music)
else:
    print ('we play the game')
    play = input("What do you like the game?")
    print("i like %r" %play)
