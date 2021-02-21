#!/bin/bash

FILETYPE=$1

BEGIN=$2

FILELIST=$(ls *.${FILETYPE})

COUNT=$((10000+${BEGIN}))

for FILE in $FILELIST;do
    NEWFILE=${COUNT}.$FILETYPE
    echo $FILE
    echo $NEWFILE
    #cp $FILE $NEWFILE
    let COUNT++
done

exit 0
