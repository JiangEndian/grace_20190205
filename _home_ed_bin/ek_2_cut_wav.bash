#!/bin/bash



FILENAME=$1
DIRNAME=$(echo $FILENAME|tr '.' '_')


mkdir $DIRNAME

./wav.py $FILENAME $DIRNAME

ls -lh $DIRNAME

echo 确认有声音的文件数量=文本的行数

read

FILENAME=$2
./wav_2.py $FILENAME $DIRNAME
ls -lh $DIRNAME
echo $DIRNAME

exit 0
