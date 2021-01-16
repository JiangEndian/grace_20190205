#!/bin/bash

ALLBYTES=0
day=1

for file in $(ls *.txt);do
    if [ $ALLBYTES -eq 0 ];then
        DIRNAME="성경第${day}天"
        ((day++))
        #echo $DIRNAME
        mkdir $DIRNAME
    fi

    BYTE=$(echo "$(ls -l $file)"|cut -d" " -f5)
    ((ALLBYTES+=BYTE))

    mv $file $DIRNAME

    if [ $ALLBYTES -gt 72542 ];then
        ALLBYTES=0
    fi

done

exit 0
