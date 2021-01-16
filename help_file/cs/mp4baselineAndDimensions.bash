#!/bin/bash

#echo $1

#1提取音频和视频文件
#ffmpeg -i $1 -acodec copy -vn output_audio.aac
#f fmpeg -i $1 -vcodec copy -an output_video.mp4

#2压缩视频文件码率至1Mbps(700K)
#ffmpeg -i output_video.mp4 -b:v 3000k -bufsize 3000k -maxrate 3200k output_video2.mp4

#3合并压缩过的视频和原始音频
#ffmpeg -i output_video2.mp4 -i output_audio.aac -vcodec copy -acodec copy $2

#4清除临时文件
#rm output_audio.aac
#rm output_video.mp4
#rm output_video2.mp4


#压缩视频文件码率至High4.2，并且降低分辨率保持比例至高为480
ffmpeg -i $1 -profile:v baseline -level 3.0 baseline3_0.mp4

#ffmpeg -i baseline3_0.mp4 -strict -2 -vf scale=-1:480 $2 #按比例，有时除不尽2就不行

ffmpeg -i baseline3_0.mp4 -strict -2 -s 854x480 $2 #不按比例，自己除下乘下大概下，
#这个是原视频的3840/2160=1.777777，*480为853.33333，直接改854得了。




