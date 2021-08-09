#!/bin/bash

if [ x$1 != x ];then
    #ffmpeg -i $1 -b 800k $2
    #ffmpeg -i $1 -vcodec libx264 -crf 24 ${2}2.mp4
    ffmpeg -i $1 -vf "scale=iw/2:ih/2" halfSizeOf_$1
    #ffmpeg -i $1 -vf "scale=iw/3:ih/3" a_third_the_frame_size.mp4
    #ffmpeg -i $1 -vf "scale=iw/4:ih/4" a_fourth_the_frame_size.mp4
else
    echo 请输入源视频/新视频的文件名作为参数
fi
