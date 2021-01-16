#!/bin/bash

./simple_print_html_canvas_cmd.py > bt.temp #第二部分先存着

cat temp.html > simple_bt.html #把后输出的第一部分先放入

cat bt.temp >> simple_bt.html #再把第二部分-主要部分放入

cat temp.html_end >> simple_bt.html #再把收尾部分放入

exit 0
