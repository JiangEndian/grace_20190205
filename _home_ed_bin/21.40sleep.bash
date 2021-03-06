#!/bin/bash
#use min..

now_time_HM()
{
    date +%H%M
}


while :;do

if [ $(now_time_HM) -eq '2140' ];then
    echo '21:40已到，请洗洗睡觉。10分钟后电脑睡眠。'
    #notify-send '21:40已到，2分钟后电脑睡眠。洗洗睡吧'
    play_once.bash ~/endring.mp3
    sleep 10m
    alarmclock.bash &
fi

sleep 2

done

exit 0
