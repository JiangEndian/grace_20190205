#!/bin/bash

testLocation(){
    eval $(xdotool getmouselocation --shell) #得到鼠标数据并且弄成变量
    #X, Y, SCREEN, WINDOW
}
#testLocation
#echo $X, $Y, $SCREEN, $WINDOW

Info='1,2,3,4,5,6为下路野区位置
7,8,9为中一塔-中间河道-对方基地
10,11,12,13,14,15为属性，黄点，4,3,2,1技能位置
16,17,18,19,20为疯脸，假腿，电锤，隐刀，BKB位置
21,22,23,24为商店位置，第二页物品位置，两行物品第一行的位置，第二行位置
'

if [ -f miniMapLocation ];then
    source miniMapLocation
else
    echo $Info
    for((i=1;i<=24;i++));do
        read -p "Press enter to record location $i in miniMapLocation after 4 seconds:"
        testLocation
        echo "X$i=$X" >> miniMapLocation
        echo "Y$i=$Y" >> miniMapLocation
    done
    exit 0
fi

moveAndClick1(){
    xdotool mousemove --sync $1 $2;sleep 0.2
    xdotool click 1;sleep 0.2
}

moveAndClick3(){
    xdotool mousemove --sync $1 $2;sleep 0.2
    xdotool click 3;sleep 0.2
}

dragFromTo(){
    xdotool keydown ctrl;sleep 0.2
    xdotool mousemove --sync $1 $2;sleep 0.2
    xdotool mousedown 1;sleep 0.2
    xdotool mousemove --sync $3 $4;sleep 0.2;
    xdotool mouseup 1;sleep 0.2
    xdotool keyup ctrl;sleep 0.2
}

getItems(){
    moveAndClick1 ${X21} ${Y21} #移动到商店并点开
    moveAndClick1 ${X22} ${Y22} #展开第二页
    dragFromTo ${X16} ${Y16} ${X23} ${Y23}
    dragFromTo ${X17} ${Y17} ${X23} ${Y23}
    dragFromTo ${X18} ${Y18} ${X23} ${Y23}
    dragFromTo ${X19} ${Y19} ${X23} ${Y23}
    dragFromTo ${X20} ${Y20} ${X23} ${Y23}
    moveAndClick1 ${X21} ${Y21} #移动到商店并点开
}

buyFirstItem(){
    moveAndClick3 ${X24} ${Y24}
    xdotool key asciitilde;sleep 0.2
    xdotool key x;sleep 0.2
    xdotool key space;sleep 0.2
}

skillUp(){
    for((i=10;i<=15;i++));do
        X="X$i"
        Y="Y$i"
        moveAndClick1 ${!X} ${!Y}
    done
}

attackForward(){
    xdotool mousemove --sync $1 $2;sleep 0.2
    xdotool key a;sleep 0.2
}

onLineFirst(){
    WT=7;notify-send -u critical starting... "after $WT seconds start onLineFirst";echo "sleep $WT";sleep $WT
    getItems
    START=$(date +%s)
    ALLTIME=$1
    let "END=START+ALLTIME*60"
    
    while [ $(date +%s) -lt ${END} ];do
        attackForward ${X8} ${Y8};sleep 2
        buyFirstItem
        skillUp
        moveAndClick3 ${X7} ${Y7};sleep 2
    done
}

autoPress1(){ #自动开启疯脸的
    START=$(date +%s)
    ALLTIME=$1
    let "END=START+ALLTIME*60"
    while [ $(date +%s) -lt ${END} ];do
        WT=17;notify-send -u critical starting... "after $WT seconds press 1";echo "sleep $WT";sleep $WT
        xdotool key 1;sleep 0.2
    done
}
    
middleJungle(){
    START=$(date +%s)
    ALLTIME=$1
    let "END=START+ALLTIME*60"

    autoPress1 $1 & #给转到后台自动运行去
    
    while [ $(date +%s) -lt ${END} ];do
        WT=7;notify-send -u critical starting... "after $WT seconds start middleJungle";echo "sleep $WT";sleep $WT
        buyFirstItem
        skillUp
        for i in 3 5 3 4 3 2 1;do
            X="X$i"
            Y="Y$i"
            xdotool mousemove --sync "${!X}" "${!Y}";sleep 0.2
            xdotool key "shift+a";sleep 0.2
        done
        WT=70;notify-send -u critical starting... "sleep $WT";echo "sleep $WT";sleep $WT
    done
}

onLineLater(){
    WT=7;notify-send -u critical starting... "after $WT seconds start onLineLater";echo "sleep $WT";sleep $WT
    START=$(date +%s)
    ALLTIME=$1
    let "END=START+ALLTIME*60"
    
    #autoPress1 $1 & #给转到后台自动运行去

    LOOPTIMES=0
    
    while [ $(date +%s) -lt ${END} ];do
        echo $LOOPTIMES
        moveAndClick3 ${X7} ${Y7};sleep 2
        attackForward ${X9} ${Y9}; echo sleep9; sleep 9

        let "LOOPTIMES++"
        if [ $LOOPTIMES -eq 10 ];then 
            buyFirstItem
            skillUp
            let "LOOPTIMES=0"
        fi
    done
}

WT=7;notify-send -u critical starting... "after $WT seconds start!";echo "sleep $WT";sleep $WT

#onLineFirst 8
#middleJungle 20
onLineLater 999

#xdotool mousemove 300 600 #移动鼠标至x,y位置
#xdotool click 3 #点击鼠标1左键，2中键，3右键，4上滚，5下滚
#xdotool key ctrl+alt+t
#xdotool mousemove_relative -- -100 100 #移动鼠标至相对于当前的位置


