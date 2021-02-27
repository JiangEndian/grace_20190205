#!/usr/bin/env python3
from newestMyPython3 import *
import struct
import array

FILENAME=getcmdargs()[0]
DIRNAME=getcmdargs()[1]

input('确认file:%s,dir:%s' % (FILENAME, DIRNAME))

#f = open('test.wav', 'rb')
f = open(FILENAME, 'rb')
info = f.read(44) #wav的开头部分

f.seek(0, 2) #指针到最末，计算长度
#print(f.tell())
#input()

n = int((f.tell() - 44) / 2)
#print(n)
buf = array.array('h', (0 for _ in range(n)))
f.seek(44)
f.readinto(buf)
#print(len(buf))
#print(buf[29107])

listTemp = []
oneFlag = False
spaceLength = 25000 #44100每1s停顿, 分割大空白的*0.n左右,小空白的1.m左右
#这个,大空白*0.n = 小空白*1.m,则大空白*0.n/小空白=1.m,大空白/小空白=1.m/0.n
#nm从1.1-9.9,则大空白是小空白的,(10+m)/n, Maximum m and Minimum n 为18倍的分割空白
#Maximum n and Minimum m 为1.12倍的分割空白.那谷哥翻译的,直接把要分割的地方,弄成两倍其他空白即可
#其实不用计算也知道,稍微大一点,然后,就那个值,就好了...为了方便设置,两倍空白,空白长度设为1.5倍的,这样比较稳点...

#关于上面的数字意义的推导...虽然是我写的,但我真的现在看不懂,得靠推测...
#44.1Khz, 44100/s * 16b(2B) = 88200B = 86KB, 单声道为22050/s * 8b(1B) = 22050B = 43KB, 
#176684B = 172KB,双声道的录音1S大小,按上面的计算, 应该是44100Khz,双声道,同时每声道16位, 嗯,44100*4=176400
#之前的这个25000怎么来的? 98860B, 98K左右,就是除以2,又除以2了吧大概.不知道为什么,可能是存储格式?
#就是98860/2/2=24715,对了.好的,那就是,98860/176400=0.56S, 就是,1S的停顿大小是176400B, 即,44100的长度
spaceNumber = 0 
fileName = 1001

#f2 = open('wavFile' + str(fileName) + '.wav', 'wb')
#f2.write(info)
#buf.tofile(f2)
#f2.close()

#exit()

for i in buf:
    listTemp.append(i)
    if abs(i) < 50:
        spaceNumber += 1
        if spaceNumber > spaceLength:
            f2 = open(DIRNAME + '/wavFile' + str(fileName) + '.wav', 'ab')
            #print('写入文件')
            f2.write(info)
            array.array('h', listTemp).tofile(f2)
            f2.close()
            fileName += 1
            spaceNumber = 0
            listTemp = []
    else:
        spaceNumber = 0



