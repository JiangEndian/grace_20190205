#!/bin/bash

if [ x$2 != x ];then
    ffmpeg -i $1 -vf reverse $2
else
    echo 请输入源视频/新视频的文件名作为参数
fi

