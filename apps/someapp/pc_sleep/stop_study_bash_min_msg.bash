#!/bin/bash


SEC=$(($1*60))

sleep $SEC && echo -e "\n\n***********$2************\n" && cvlc "/home/endian/alarm.mp3"

exit
