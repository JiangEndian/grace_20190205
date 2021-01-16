#!/bin/bash
#use min..

SEC=$(($1*60))

echo jf3333333777|sudo -S rtcwake -m mem -s $SEC
#sleep this pc,and wake it after the SEC

sleep 3
#rest 3s when wake up...

cvlc "/home/endian/alarm.mp3"
#play this music...
