#!/bin/bash

DATE=`date +%Y%m%d`

DIR='/media/ed/Kindle/documents/'

FILE=${DIR}${DATE}_year.txt

#echo $FILE

#exit 0
#./print_내일_common.py > $FILE && echo 'Print_Succese'
./year_ndays_restudy_print내일.py > $FILE && echo 'Print_Succese'

#umount /media/ed/Kindle

exit 0
