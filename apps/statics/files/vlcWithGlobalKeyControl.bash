#!/bin/bash

#cp $1 /dev/shm/ #复制文件到内存文件系统加快访问速度
sudo vlc --global-key-jump-short q --global-key-jump+medium w $1 #后退10s的short与前进1min的medium

