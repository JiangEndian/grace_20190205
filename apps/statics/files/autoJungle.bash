#!/bin/bash

testLocation(){
    eval $(xdotool getmouselocation --shell) #得到鼠标数据并且弄成变量
    #X, Y, SCREEN, WINDOW
}
#testLocation
#echo $X, $Y, $SCREEN, $WINDOW

#打野循环顺序为1,2,3,4,循环，获取4个位置的变量##################
if [ -f miniMapLocation ];then
    source miniMapLocation
    for((i=1;i<5;i++));do
        X="X$i"
        Y="Y$i"
        echo "${!X}", "${!Y}" #神奇的引用变量里的字符串名的变量。。。
    done
    read -p 'location data exist, press enter.'
else
    for((i=1;i<5;i++));do
        read -p "Press enter to record location$i in miniMapLocation after 4 seconds:"
        sleep 4

        notify-send 'last 2 seconds'
        sleep 2

        testLocation
        echo "X$i=$X" >> miniMapLocation
        echo "Y$i=$Y" >> miniMapLocation
    done
fi
#打野循环顺序为1,2,3,4,循环，获取4个位置的变量##################

echo 'After 6 seconds auto Jungle 10 times in 10 minutes...'
sleep 6

#根据四个位置的变量反复的移动并shift+a，一次10遍############
for((i=0;i<10;i++));do #直接反复的循环，来个10遍一次
    for((i=1;i<5;i++));do
        X="X$i"
        Y="Y$i"
        echo "${!X}" "${!Y}"
        xdotool mousemove --sync "${!X}" "${!Y}"
        sleep 1
        echo "shift+a"
        xdotool key "shift+a"
        sleep 1
    done
    notify-send 'sleep 60s'
    sleep 60
done
#根据四个位置的变量反复的移动并shift+a，一次10遍############


#xdotool mousemove 300 600 #移动鼠标至x,y位置
#xdotool click 3 #点击鼠标1左键，2中键，3右键，4上滚，5下滚
#xdotool key ctrl+alt+t
#xdotool mousemove_relative -- -100 100 #移动鼠标至相对于当前的位置


