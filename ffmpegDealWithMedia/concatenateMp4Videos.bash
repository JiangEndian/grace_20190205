#!/bin/bash

if [ x$3 != x ];then
    ffmpeg -i $1 -c copy -bsf:v h264_mp4toannexb -f mpegts temp1.ts
    ffmpeg -i $2 -c copy -bsf:v h264_mp4toannexb -f mpegts temp2.ts
    ffmpeg -i "concat:temp1.ts|temp2.ts" -c copy -bsf:a aac_adtstoasc $3 
    rm temp1.ts; rm temp2.ts
else
    echo 请输入源视频1/源视频2/新视频的文件名作为参数
fi




