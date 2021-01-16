#!/bin/bash

TEMP='read4line_temp'

grep '[()（）[]' $1 > $TEMP


ALLLINE=$(wc -l $TEMP | cut -d" " -f1)

for((i=1;i<=ALLLINE;i++));do
    clear
    #head -n$i $TEMP | tail -n1 | grep --color=auto '[(（[]'
    head -n$i $TEMP | tail -n1 | grep --color=auto '[()（）[]'
    read
done

echo ${1}_完
read

exit 0
