#!/bin/bash

DATE=`date +%Y%m%d`

DIR='/media/ed/Kindle/documents/'

FILE=${DIR}${DATE}.txt

#echo $FILE

./print_내일_common.py > $FILE && echo 'Print_Succese'

#umount /media/ed/Kindle

exit 0
