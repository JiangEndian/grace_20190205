#!/bin/bash

LIGHT=`cat light.conf`

if [ $LIGHT -eq 99 ];then
	exit 0
fi
let LIGHT+=11

echo $LIGHT > light.conf

./light

exit 0
