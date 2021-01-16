#!/bin/bash

readoneline() #读取一行
{
    head -n$1  koreanlite4bash.txt | tail -n1
}

BEGIN=$(cat read) #上次放到哪儿了（第几行）

for((i=$BEGIN;i<1166;i++));do
    clear #清个屏先
    let num=1 #计算遍历到第几个，第一个的话用来放音
    #echo $(readoneline $i)
    for text in $(readoneline $i);do
        if [ $num -eq 1 ];then
            AUDIO=$text
            cvlc -R --no-repeat --play-and-exit $text.mp3 > /dev/null 2>&1 &
        else 
            echo $text | tr '_' ' ' #再换回空格
        fi
        let num++ #使她不是1就行，这里用了++，其实=2也行
    done

    echo $i > read #放完一行，记录下此行（第几行）

    while read && [[ $REPLY != 'n' ]];do #显示完判断是否进入下一条
        cvlc -R --no-repeat --play-and-exit $AUDIO.mp3 > /dev/null 2>&1 &
    done

done

