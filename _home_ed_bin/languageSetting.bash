#!/bin/bash
#用法为在bash终端下 source languageSetting.bash
#不然就是在程序的一个新bash里执行了。。。白费
lang_input=en_US.UTF-8
LANG=$lang_input
LANGUAGE=`echo $LANG|awk -F. '{print $1}'`
LC_CTYPE=$lang_input
LC_NUMERIC=$lang_input
LC_TIME=$lang_input
LC_COLLATE="$lang_input"
LC_MONETARY=$lang_input
LC_MESSAGES="$lang_input"
LC_PAPER=$lang_input
LC_NAME=$lang_input
LC_ADDRESS=$lang_input
LC_TELEPHONE=$lang_input
LC_MEASUREMENT=$lang_input
LC_IDENTIFICATION=$lang_input
