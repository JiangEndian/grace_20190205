#!/usr/bin/env python3

textA = '''

'''

textB = '''

'''

list_textA = textA.split('\n')
list_textB = textB.split('\n')

for lineA, lineB in zip(list_textA, list_textB):
    print(lineA)
    print(lineB)

