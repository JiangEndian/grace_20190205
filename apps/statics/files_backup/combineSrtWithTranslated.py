#!/usr/bin/env python3
import sys
import re
test = r'(.*[ +].*),([\u4e00-\u9fa5]+.*)'
han = r'.*[\u4e00-\u9fa5].*'

K1 = False
Z1 = False
K2 = False
Z2 = False

char_num = 0

Is2 = True

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]

all_character = 5000
if not file_name1 or not file_name2:
    print('没有文件')
    exit()

last_one_size = 0
eligible_amount = 0
line_number = 0

lineCircle = 1
with open(file_name1, 'r') as f1:
    with open(file_name2, 'r') as f2:
        f2lines = f2.readlines()
        for line in f1.readlines(): 
            line_number += 1
            if line_number % lineCircle == 0:
                print(f2lines[line_number//lineCircle-1].strip())
            print(line.strip())


        #为了应对新形式的文本，是有大量空行的，直接过滤掉
        #if line == '':
            #continue

        #if re.match(han, line):
