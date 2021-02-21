#!/bin/bash

./print_html_canvas_cmd.py > bt.temp #第二部分先存着

cat temp.html > bt.html #把后输出的第一部分先放入

cat bt.temp >> bt.html #再把第二部分-主要部分放入

cat temp.html_end >> bt.html #再把收尾部分放入

exit 0
