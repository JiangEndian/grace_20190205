#!/bin/bash

LIST=$(ls *.wav)
#echo $LIST

clear

for i in $LIST; do
    echo $i
    cvlc -R --no-repeat --play-and-exit $i >/dev/null 2>&1 
    read
    cvlc -R --no-repeat --play-and-exit $i >/dev/null 2>&1 
done

exit 0
