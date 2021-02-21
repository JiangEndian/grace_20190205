#!/bin/bash

while :;do
    clear

    PROCESS=$(ps -aux|grep 'cinnamon --replace --replace'|head -n1)
    
    MEM=$(echo $PROCESS | cut -d' ' -f4| cut -d '.' -f 1)
    
    #echo $MEM
    
    if [ $MEM -gt 7 ];then
        echo $MEM
        notify-send $MEM
    fi

    sleep 30m
done

exit 0
