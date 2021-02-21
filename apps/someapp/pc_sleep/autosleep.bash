#!/bin/bash
#use min..

if [ -n "$1" ];then
    echo "PC将sleep至${1}分钟之后"
    sleep 10
    SEC=$(($1*60))
    echo jf3333333777|sudo -S rtcwake -m mem -s $SEC
    #echo $1
    #exit 0
else
    echo '$1没有,PC将sleep至次日5：50' 
    sleep 10
    echo jf3333333777|sudo -S rtcwake -m mem -s $(now2tomorrow.py)  #自带的时间设置极其诡异，用这个完全有效，很好用。
fi

exit 0

#echo jf3333333777|sudo -S rtcwake -m mem -s $(./now2tomorrow.py)
#echo jf3333333777|sudo -S rtcwake -m mem -s $SEC
#sleep this pc,and wake it after the SEC

#sleep 3
#rest 3s when ring......

#cvlc "/home/endian/alarm.mp3"
#play this music...
