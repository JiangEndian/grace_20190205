#!/bin/bash

flag4multi=0
multi=0

#文本规则是经节位置，然后多节的，在开始之前写下节数，如：verses:
#创世纪 1-1 #创世纪1章1节
#3
#出埃及记 2-1 #出埃及记 2章1-3节

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

