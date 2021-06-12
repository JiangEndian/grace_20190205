#!/bin/bash

Seconds=$(date +%s)
echo $Seconds

if [ x$2 != x ];then
    ffmpeg -i $1 -c copy -an audioRemoved.mp4
    ffmpeg -i audioRemoved.mp4 -vf reverse reversed${Seconds}.mp4
    ffmpeg -i audioRemoved.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp1.ts
    ffmpeg -i reversed${Seconds}.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts temp2.ts
    ffmpeg -i "concat:temp1.ts|temp2.ts" -c copy -bsf:a aac_adtstoasc $2
    rm temp1.ts; rm temp2.ts; rm audioRemoved.mp4; 
else
    echo 请输入源视频/新视频的文件名作为参数
fi
