#!/bin/bash

ifconfig

read -p "input the name of the wireless card that you wanna turn off:"

echo jf3333333777|sudo -S ifconfig $REPLY down


