#!/usr/bin/python3

import os

foldername = input('Folder Name: ')

filenames = os.listdir(foldername)
filenames.sort()

filesizes = []
for filename in filenames:
    filesizes.append(os.path.getsize(foldername+'/'+filename))

print('Please input texts, end by YES:')
texts = []
ISLine1 = True
while True:
    text = input()
    if text == 'YES':
        break
    if ISLine1:
        texts.append(text)
    ISLine1 = not ISLine1

for linenumber in range(len(texts)):
    #print(linenumber)
    percentage = filesizes[linenumber] / len(texts[linenumber])
    print(filenames[linenumber] + ' ' + str(percentage))

print(foldername)
#print(filenames, filesizes, texts)

