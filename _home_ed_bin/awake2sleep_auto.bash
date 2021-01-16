#!/bin/bash

now_time_HM()
{
    date +%H%M
}

#between those PC sleep...
MORNING='0550'
FORENOON='0600'

morning_sleep_noon_alarm()
{
    if [ $(now_time_HM) -gt $MORNING -a $(now_time_HM) -lt $FORENOON ];then
        #alarmclock.bash 470 #13:50分(之前)闹醒
        echo $(now_time_HM):alarmclock.bash_470运行，睡上470分钟
    fi
}


#between those PC sleep...
NOON='1350'
AFTERNOON='1400'

noon_sleep_evening_wake()
{
    if [ $(now_time_HM) -gt $NOON -a $(now_time_HM) -lt $AFTERNOON ];then
        #autosleep.bash 420 #21点(之前)醒来
        echo $(now_time_HM):autosleep.bash_420运行，睡上420分钟
    fi
}


while :;do
    morning_sleep_noon_alarm
    noon_sleep_evening_wake
    sleep 1m
done
