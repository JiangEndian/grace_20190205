#!/bin/bash

flag4multi=0
multi=0

#文本规则是经节位置，然后多节的，在开始之前写下节数

cat verses | while read line
do
    if [ `echo $line | wc -L` -gt 3 ];then
        if [ $flag4multi -eq 1 ];then
            grep -A $multi "$line " chinese_bible.txt
            echo
            flag4multi=0
        else
            grep "$line "  chinese_bible.txt
            echo;echo
        fi
    
    else
        flag4multi=1
        multi=$(($line*2-1))
    fi

done

