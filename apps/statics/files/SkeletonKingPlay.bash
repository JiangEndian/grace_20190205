#!/bin/bash

testLocation(){
    eval $(xdotool getmouselocation --shell) #得到鼠标数据并且弄成变量
    #X, Y, SCREEN, WINDOW
}
#testLocation
#echo $X, $Y, $SCREEN, $WINDOW

#打野循环顺序为1,2,3,4,5循环，6, 7 is the location of Home and Enemy
if [ -f miniMapLocation ];then
    source miniMapLocation
else
    for((i=1;i<=7;i++));do
        read -p "Press enter to record location$i in miniMapLocation after 4 seconds:"
        sleep 4

        notify-send -u critical 2seconds "record location after 2 seconds"
        sleep 2

        testLocation
        echo "X$i=$X" >> miniMapLocation
        echo "Y$i=$Y" >> miniMapLocation
    done
    exit 0
fi

#level up skill, and press skill
skillUpPlay(){
    xdotool key ctrl+v; sleep 0.1
    xdotool key ctrl+r; sleep 0.1
    xdotool key ctrl+e; sleep 0.1
    xdotool key ctrl+t; sleep 0.1
    xdotool key v;sleep 0.5
}

#smallJungle Once, 1-2-3
smallJungle(){
    #for((i=1;i<=3;i++));do
    for i in 1 2 1 2 1 2 3;do
        X="X$i"
        Y="Y$i"
        xdotool mousemove --sync "${!X}" "${!Y}"
        sleep 0.3
        xdotool key "shift+a"
        sleep 0.3
    done
    xdotool mousemove --sync "${XM}" "${YM}"
    xdotool click 1
    sleep 0.1
    xdotool click 1
}
    
#middleJungle Once, 2-5, 2-3-4-5-2
middleJungle(){
    #for((i=1;i<=5;i++));do
    for i in 3 2 3 4 3 5 3 2 3 4 3 5;do
        X="X$i"
        Y="Y$i"
        xdotool mousemove --sync "${!X}" "${!Y}"
        sleep 0.3
        xdotool key "shift+a"
        sleep 0.3
    done
}

onLine(){
    while :;do
        skillUpPlay

        X="X6"
        Y="Y6"
        xdotool mousemove --sync "${!X}" "${!Y}"
        sleep 0.3
        xdotool click 3
        echo "sleep 20"
        sleep 20
        notify-send -u critical attackOnline "after backHome, attackOnline"

        X="X7"
        Y="Y7"
        xdotool mousemove --sync "${!X}" "${!Y}"
        sleep 0.3
        xdotool key a
        echo "sleep 30"
        sleep 30 #总50.6秒，正好对应V技能
    done
}

#earlyTime autoJungle
earlyTime(){
    for((j=0;j<3;j++));do
        echo $j
        notify-send -u critical 7seconds "after 7 seconds start smallJungle"
        echo "sleep 7"
        sleep 7
        skillUpPlay
        smallJungle
        ET=120
        notify-send -u critical ${ET}seconds "sleep for ${ET} seconds"
        echo "sleep for ${ET} seconds"
        sleep ${ET}
        xdotool key 2 
        sleep 0.1
    done
}

#middleTime autoJungle
middleTime(){
    for((j=0;j<7;j++));do
        echo $j
        notify-send -u critical 7seconds "after 7 seconds start middleJungle"
        echo "sleep 7"
        sleep 7
        skillUpPlay
        middleJungle
        MT=120
        notify-send -u critical ${MT}seconds "sleep for ${MT} seconds"
        echo "sleep for ${MT} seconds"
        sleep ${MT}
    done
}

#laterTime autoJungle
laterTime(){
    for((j=0;j<7;j++));do
        echo $j
        notify-send -u critical 7seconds "after 7 seconds start middleJungle"
        echo "sleep 7"
        sleep 7
        skillUpPlay
        middleJungle
        MT=70
        notify-send -u critical ${MT}seconds "sleep for ${MT} seconds"
        echo "sleep for ${MT} seconds"
        sleep ${MT}
    done
}

WT=120
notify-send -u critical starting... "after $WT seconds start!"
echo "sleep $WT"
sleep $WT

earlyTime
middleTime
laterTime
onLine

#xdotool mousemove 300 600 #移动鼠标至x,y位置
#xdotool click 3 #点击鼠标1左键，2中键，3右键，4上滚，5下滚
#xdotool key ctrl+alt+t
#xdotool mousemove_relative -- -100 100 #移动鼠标至相对于当前的位置


