#!/bin/bash

TIME="+9day9:50"

if [ -n "$2" ];then
    TO=`date -d $TIME +%s`
    echo jf3333333777|sudo -S rtcwake -m mem -t $TO

    exit 0

fi


if [ -n "$1" ];then
    echo "PC将sleep至${1}分钟之后"
    sleep 10
    echo jf3333333777|sudo -S rtcwake -m mem --date +${1}min
else
    TO=`date -d $TIME +%s`
    echo '$1'没有,PC将sleep至$(date -d $TIME)
    sleep 10
    echo jf3333333777|sudo -S rtcwake -m mem -t $TO
fi

sleep 60

exit 0

