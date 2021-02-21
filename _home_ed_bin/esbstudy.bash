#!/bin/bash

TEMP='esb_temp4grep_file'

grep '\[' $1 > $TEMP


#grep --color=auto '[^a-zA-Z0-9.:",;；!]' esb_temp4grep_file


#exit 0




ALLLINE=$(wc -l $TEMP | cut -d" " -f1)

clear

for((i=1;i<=ALLLINE;i++));do
    ONELINE=$(head -n$i $TEMP | tail -n1)
    #echo $ONELINE
        clear
        echo "$ONELINE" | grep --color=auto '[^a-zA-Z0-9.:",; !]'
        read
done

clear
echo $1

exit 0
