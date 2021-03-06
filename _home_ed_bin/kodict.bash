#!/bin/bash

for i;do
    #echo $i
    chromium-browser "http://cndic.naver.com/search/all?q=$i"
done

exit 0
