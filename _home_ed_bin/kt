#!/usr/bin/env python3
from newestMyPython3 import *
from datetime import datetime

hnow = int(datetime.now().strftime('%H'))%12
#print(hnow)
mnow = int(datetime.now().strftime('%M'))
#print(mnow)

#exit()

hour = '한시 두시 세시 네시 다섯시 여섯시 일곱시 여덟시 아홉시 열시 열한시 열두시 한시'.split()

one = '일 이 삼 사 오 육 칠 팔 구'.split()

two = '십 이십 삼십 사십 오십 육십 칠십'.split()
hi=hnow - 1
#for h in hour:
h = hour[hnow-1]
    #for i in range(60):
i = mnow
if True:
    if True:
        #i=55    #中断测试
        if i == 0:
            print(h)
        elif i == 30:
            print(h+'_'+'삼십분')
            print(h+'_'+'반')
        elif i < 10:
            print(h+'_'+one[i-1]+'분')
        elif i < 30 :
            if i % 10 == 0:
                print(h+'_'+two[i//10-1]+'분')
            else:
                print(h+'_'+two[i//10-1]+one[i%10-1]+'분')
        else:
            if i % 10 == 0:
                print(h+'_'+two[i//10-1]+'분')
                if i>40:
                    print(hour[hi+1]+'_'+two[((60-i)//10-1)]+'분전')
            else:
                #print(i)
                print(h+'_'+two[i//10-1]+one[i%10-1]+'분')
                if i>40 and i%5==0:
                    if i==55:
                        print(hour[hi+1]+'_'+one[(60-i)%10-1]+'분전')
                    else:
                        print(hour[hi+1]+'_'+two[(60-i)//10-1]+one[(60-i)%10-1]+'분전')
        #input()
    #hi+=1
            #
                
