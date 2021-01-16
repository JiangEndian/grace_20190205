#!/usr/bin/env python3
from datetime import datetime, timedelta

now = datetime.now()    #

tomorrow = now + timedelta(days=1)
alarmymd = tomorrow.strftime('%Y%m%d')  #格式化时间为年月日

#alarm = datetime.strptime(alarmymd + ' 5:50:00', '%Y%m%d %H:%M:%S') #tomorrow5:50m...
alarm = datetime.strptime(alarmymd + ' 6:40:00', '%Y%m%d %H:%M:%S') #tomorrow6:40m...

sleeptime = alarm.timestamp() - now.timestamp()

print(int(sleeptime))
#print(2500)

