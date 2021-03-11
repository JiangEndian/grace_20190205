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

file_name = sys.argv[1]

all_character = 5000
if not file_name:
    print('没有文件')
    exit()

with open(file_name, 'r') as f:
    for line in f.readlines(): 
        Is2 = not Is2
        line = line.strip()+'. '
        #line = line.strip()

        #为了应对新形式的文本，是有大量空行的，直接过滤掉
        #if line == '':
            #continue

        #if re.match(han, line):
        if Is2:
            #new_line = '('+line+').'
            new_line = ''
            print(new_line)
            #char_num += len(new_line)
            char_num += 1
            if char_num > 4940:
                #print('4900')
                #char_num = 0
                pass
                #input()
        else: #提前判断这一行会不会超5000,超出的话提示之
            if char_num + len(line) > all_character:
                print(all_character)
                char_num = 0
            print(line)
            char_num += len(line)
            char_num += 1
        continue
            

        
        #if re.match(test, line):
            #m = re.match(test, line)
            #print(m.group(0))
            #print(m.group(1))
            #print(m.group(2))
            #input()
        #else:
            #continue
            #print(line)
        #continue
        
        if '）ㄱ：' in line and not K1:
            K1 = line
            continue
            #print(line)
            #input()
        elif not K1:
            print(line)
        
        if K1 and Z1 and K2 and not Z2:
            Z2 = line
            print(K1+K2,'\n', Z1+','+Z2)
            K1 = False
            Z1 = False
            K2 = False
            Z2 = False
            #input()
        elif K1 and Z1 and not K2:
            K2 = line
        elif K1 and not Z1:
            Z1 = line
        elif K1 and Z1 and K2 and Z2:
            print(K1+K2,'\n', Z1+','+Z2)
            K1 = False
            Z1 = False
            K2 = False
            Z2 = False
            #input()


