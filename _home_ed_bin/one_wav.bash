#!/bin/bash



FILENAME=$1
DIRNAME=$(echo $FILENAME|tr '.' '_')


mkdir $DIRNAME

mv $FILENAME $DIRNAME

ls -lh $DIRNAME

echo 确认有声音的文件数量=文本的行数

echo $DIRNAME

exit 0
