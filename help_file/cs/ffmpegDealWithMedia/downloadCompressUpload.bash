#!/bin/bash

dir='forPostUpload'
wget -O $1 historyofsalvation.oss-cn-hongkong-internal.aliyuncs.com/$dir/$1 && ffmpeg -i $1 -vf "scale=iw/2:ih/2" ${1}_half_size.mp4 && mv ${1}_half_size.mp4 $1 && ./ossutil64 cp $1 oss://historyofsalvation/$dir/$1
#./ossutil64 cp $1 oss://historyofsalvation/$dir/$1

