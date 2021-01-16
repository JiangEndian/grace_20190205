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

file_name1 = sys.argv[1]

flag1_135 = True
num1 = 0
num2 = 0

with open(file_name1, 'r') as f1:
    for line1 in f1.readlines(): 
        num1 += 1
        line1 = line1.strip()
        if flag1_135:
            print(line1)
            flag1_135 = not flag1_135
        else:
            flag1_135 = not flag1_135
            continue

