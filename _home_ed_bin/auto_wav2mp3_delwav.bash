#!/bin/bash

dir_wav2mp3(){
    cd $1
    for file in $(ls *.wav);do
        if [ ! -f ${file}.mp3 ];then
            echo ${file}.mp3
            lame $file ${file}.mp3
        fi
    done

    for file in $(ls *.wav);do
        if [ -f ${file}.mp3 ];then
            rm ${file}
        fi
    done
    cd ..
}

for dir in $(ls);do
    if [ -d $dir ];then
        #echo $dir
        #read
        dir_wav2mp3 $dir
    fi
done

rm *.wav

exit 0
