#!/usr/bin/env python3
from newestMyPython3 import *
import struct
import array

FILENAME=getcmdargs()[0]
DIRNAME=getcmdargs()[1]

input('确认file:%s,dir:%s' % (FILENAME, DIRNAME))

#f = open('test.wav', 'rb')
f = open(FILENAME, 'rb')
info = f.read(44)

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
spaceLength = 35000
spaceNumber = 0 
fileName = 1001

#f2 = open('wavFile' + str(fileName) + '.wav', 'wb')
#f2.write(info)
#buf.tofile(f2)
#f2.close()

#exit()

for i in buf:
    listTemp.append(i)
    if abs(i) < 20:
        spaceNumber += 1
        if spaceNumber > spaceLength:
            f2 = open(DIRNAME + '/wavFile' + str(fileName) + '.wav', 'ab')
            #print('写入文件')
            #f2.write(info)
            array.array('h', listTemp).tofile(f2)
            f2.close()
            fileName += 1
            spaceNumber = 0
            listTemp = []
    else:
        spaceNumber = 0



