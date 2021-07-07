#!/bin/bash

#if [ x$2 != x ];then
    #ffmpeg -i $1 -b 800k $2
    #ffmpeg -i $1 -vcodec libx264 -crf 24 ${2}2.mp4
    #ffmpeg -i $1 -vf "scale=iw/2:ih/2" half_the_frame_size.mp4
    #ffmpeg -i $1 -vf "scale=iw/3:ih/3" a_third_the_frame_size.mp4
    #ffmpeg -i $1 -vf "scale=iw/4:ih/4" a_fourth_the_frame_size.mp4
#else
#fi

for f in *.mp4; do 
    ffmpeg -i $f -vf "scale=iw/2:ih/2" ${f}_half_size.mp4
done
