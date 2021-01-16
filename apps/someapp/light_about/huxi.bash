#!/bin/bash

sleep 3

x=$(cat /dev/shm/light_num)
for((;x>=0;x--));do
    light_num $(($x*$x/100))
    sleep 0.001
done

sleep 7

while :;do
    for((x=0;x<=99;x++));do
        light_num $(($x*$x/100))
        echo $x > /dev/shm/light_num &
    done
    
    sleep 1

    for((x=-99;x<=0;x++));do
        light_num $(($x*$x/100))
        echo $x > /dev/shm/light_num &
        done

    sleep 7
done

exit 0
