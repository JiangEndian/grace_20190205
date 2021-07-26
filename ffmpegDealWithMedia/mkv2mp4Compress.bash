#!/bin/bash

#参数1源视频2新视频


if [ x$2 != x ];then
    #ffmpeg -i $1 -codec copy $2 #只是换个mp4的壳，大小几乎不变
    ffmpeg -i $1 -vcodec libx265 -crf 28 $2 #降低ConstantRateFactor至28
    #上面这个压缩的太狠了，电脑能打开，但浏览器根本不行。。。

    #还有别的，能压缩宽高的
    #ffmpeg -i input.mkv -vf "scale=iw/2:ih/2" half_the_frame_size.mkv
    #ffmpeg -i input.mkv -vf "scale=iw/3:ih/3" a_third_the_frame_size.mkv
    #ffmpeg -i input.mkv -vf "scale=iw/4:ih/4" a_fourth_the_frame_size.mkv
    
    #还有能降低码率的
    #ffmpeg -i input.mp4 -b 800k output.mp4

else
    echo 请输入源视频/新视频的文件名作为参数
fi
