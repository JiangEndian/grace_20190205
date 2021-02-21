#!/bin/bash

echo normal,inverted,left,right,0,2,1,3

read -p "Select rotation mode:" 

xrandr -o $REPLY


