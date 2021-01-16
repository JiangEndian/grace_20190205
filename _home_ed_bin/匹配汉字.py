#!/usr/bin/env python3

import re
import sys

for teststring in sys.argv[1:]:
    #print(teststring)
    if re.match(r'.*[\u4e00-\u9fa5].*', teststring):
        print('YES')
        exit()
print('NO')

