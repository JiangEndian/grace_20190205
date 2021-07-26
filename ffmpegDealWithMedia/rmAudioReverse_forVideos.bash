#!/bin/bash

Seconds=$(date +%s)

cd ~/forVideos
for i in *;do
    ffmpeg -i $i -vf reverse reversed_$i
done

