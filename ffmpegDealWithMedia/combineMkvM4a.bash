#!/bin/bash

#参数1源视频2源音频3新视频

if [ x$3 != x ];then
    ffmpeg -i $1 -c copy -an tempVideoWithoutAudio.mkv
    ffmpeg -i tempVideoWithoutAudio.mkv -i $2 -c:v copy -c:a aac $3
    rm tempVideoWithoutAudio.mkv
else
    echo 请输入源视频/源音频/新视频的文件名作为参数
fi
