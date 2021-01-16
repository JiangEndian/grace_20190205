#!/bin/bash
#use min..

if [ -n "$1" ];then
    echo "PC将sleep至${1}分钟之后"
    sleep 10
    echo jf3333333777|sudo -S rtcwake -m mem --date +${1}min
else
    TIME="+1day05:50"
    TO=`date -d $TIME +%s`
    echo '$1'没有,PC将sleep至$(date -d $TIME)
    sleep 10
    echo jf3333333777|sudo -S rtcwake -m mem -t $TO
fi

sleep 3

play_once.bash ~/beginring.mp3
exit 0

