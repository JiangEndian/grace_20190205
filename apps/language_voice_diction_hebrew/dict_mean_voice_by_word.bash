#!/bin/bash

clear

FNAME='hebrew_2018/'$1

FNAME=$(echo $FNAME | tr ' ' '+')

cd /home/ed/grace/apps/language_voice_diction_hebrew && ./mean_voice_by_word.py $FNAME

exit 0
