#!/usr/bin/env python3
import sys
import re
test = r'(.*[ +].*),([\u4e00-\u9fa5]+.*)'
han = r'.*[\u4e00-\u9fa5].*'
#if re.match(han, line):

K1 = False
Z1 = False
K2 = False
Z2 = False

char_num = 0

Is2 = True

file_name = sys.argv[1]

all_character = 5000
if not file_name:
    print('没有文件')
    exit()

last_one_size = 0
eligible_amount = 0
line_number = 0
lastOddLine = ''
continueAgain = False

with open(file_name, 'r') as f:
    for line in f.readlines(): 
        line_number += 1
        Is2 = not Is2
        #line = line.strip()+'. '
        line = line.strip()

        if continueAgain:
            continueAgain = False
            continue


        if not Is2:
            if line == lastOddLine:
                continueAgain = True
                #print('same')
                continue
            lastOddLine = line
            print(lastOddLine)
        elif True:
            print(line)
            pass
        else: #提前判断这一行会不会超5000,超出的话提示之
            #if char_num + len(line) > all_character:
                #print(all_character)
                #char_num = 0
            if re.match(han, line):
                print('有汉字', line)
                print(line_number)
                exit(0)
            if len(line) > 900:
                print(line, str(len(line))+':太多了需要分割')
                print(line_number)
                print()
            elif len(line) > 10:
                eligible_amount += 1
            #if last_one_size > 0 and last_one_size+len(line)<900:
                #print(line, '可与上个合并')
                #print()
            last_one_size = len(line)
            #char_num += len(line)
            #char_num += 1
        continue
#print('合格的：'+str(eligible_amount))
