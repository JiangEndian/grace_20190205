#!/bin/bash

for filename;do
echo $filename
wget -O $filename historyofsalvation.oss-cn-hongkong-internal.aliyuncs.com/$filename
done
