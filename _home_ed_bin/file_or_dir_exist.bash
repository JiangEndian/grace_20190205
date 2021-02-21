#!/bin/bash

if [ -x $1 ] || [ -d $1 ];then
    exit 0
else
    exit 222
fi

