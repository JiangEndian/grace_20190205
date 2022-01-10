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

#buy item in the first place of shop
buyFirstItem(){
    xdotool mousemove --sync "${XItem0}" "${YItem0}"
    xdotool click 3;sleep 0.1
    xdotool key x;sleep 0.1
}

#level up skill, and press skill
skillUpPlay(){
    buyFirstItem
    xdotool key ctrl+v; sleep 0.1
    xdotool key ctrl+r; sleep 0.1
    xdotool key ctrl+e; sleep 0.1
    xdotool key ctrl+t; sleep 0.1
    #xdotool key v;sleep 0.5
}

#smallJungle Once, 1-2-3
smallJungle(){
    for i in 1 2 3 2 3;do
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
    for i in 3 5 3 4 3 2 1;do
        X="X$i"
        Y="Y$i"
        xdotool mousemove --sync "${!X}" "${!Y}"
        sleep 0.3
        xdotool key "shift+a"
        sleep 0.1
    done
    xdotool key "shift+v" #每波过后，来次v技能
    sleep 0.1
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
        sleep 15
        notify-send -u critical attackOnline "after backHome, attackOnline"

        X="X7"
        Y="Y7"
        xdotool mousemove --sync "${!X}" "${!Y}"
        sleep 0.3
        xdotool key a
        echo "sleep 35"
        sleep 30 #总50.6秒，正好对应V技能
    done
}

onLineDown(){
    skillUpPlay
    for((j=0;j<20;j++));do

        xdotool mousemove --sync "${XDown1}" "${YDown1}"
        sleep 0.3
        xdotool key a
        echo "sleep 5"
        sleep 5 

        X="XDown0"
        Y="YDown0"
        xdotool mousemove --sync "${XDown0}" "${YDown0}"
        sleep 0.3
        xdotool click 3
        echo "sleep 10"
        sleep 10
        notify-send -u critical attackOnline "after backHome, attackOnline"

    done
    skillUpPlay
    xdotool key t
    xdotool key e
}

#earlyTime autoJungle
earlyTime(){
    for((j=0;j<2;j++));do
        echo $j
        notify-send -u critical 7seconds "after 7 seconds start smallJungle"
        echo "sleep 7"
        sleep 7
        skillUpPlay
        smallJungle
        ET=90
        notify-send -u critical ${ET}seconds "sleep for ${ET} seconds"
        echo "sleep for ${ET} seconds"
        sleep ${ET}
        xdotool key 2 
        sleep 0.1
    done
}

#middleTime autoJungle
middleTime(){
    for((j=0;j<99;j++));do
        echo $j
        notify-send -u critical 7seconds "after 7 seconds start middleJungle"
        echo "sleep 7"
        sleep 7
        skillUpPlay
        middleJungle
        middleJungle
        middleJungle
        middleJungle
        MT=$((540-j*60)) #上限为34次，一次中级是8次，4次差不多，看看9分钟能不能搞定。
        notify-send -u critical ${MT}seconds "sleep for ${MT} seconds"
        echo "sleep for ${MT} seconds"
        sleep ${MT}
    done
}

#laterTime autoJungle
laterTime(){
    for((j=0;j<9;j++));do
        echo $j
        notify-send -u critical 7seconds "after 7 seconds start middleJungle"
        echo "sleep 7"
        sleep 7
        skillUpPlay
        middleJungle
        MT=80
        notify-send -u critical ${MT}seconds "sleep for ${MT} seconds"
        echo "sleep for ${MT} seconds"
        sleep ${MT}
    done
}

WT=7
notify-send -u critical starting... "after $WT seconds start!"
echo "sleep $WT"
sleep $WT

#onLineDown
#earlyTime
middleTime
laterTime
onLine

#xdotool mousemove 300 600 #移动鼠标至x,y位置
#xdotool click 3 #点击鼠标1左键，2中键，3右键，4上滚，5下滚
#xdotool key ctrl+alt+t
#xdotool mousemove_relative -- -100 100 #移动鼠标至相对于当前的位置


