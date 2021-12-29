#!/bin/bash

aForward(){
    xdotool mousemove_relative --sync -- 400 -300
    xdotool key a
}

moveBackward(){
    xdotool mousemove_relative --sync -- -400 300
    xdotool click 3
}

for((i=7;i>=1;i--));do
    echo "after $i second started..."
    notify-send "after $i second started..."
    sleep 1
done

while true;do
    aForward
    sleep 3
    moveBackward
    sleep 3
done

#xdotool mousemove 300 600 #移动鼠标至x,y位置
#xdotool click 3 #点击鼠标1左键，2中键，3右键，4上滚，5下滚
#xdotool key ctrl+alt+t
#xdotool mousemove_relative -- -100 100 #移动鼠标至相对于当前的位置


