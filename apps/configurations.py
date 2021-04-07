#!/usr/bin/env python3

from MyPython3 import *


def readConfigurations(FileName):
    Configurations = {'InfoOfThisConfigurations':'This is a dictionary to story configurations.'}
    if os.path.exists(FileName):
        Configurations = loadffile(FileName)
    else:
        dump2file(FileName, Configurations)
    return Configurations

def updateConfigurations(FileName, Configurations, UpdateDictionsary):
    Configurations = loadffile(FileName)
    for Key in UpdateDictionsary:
        Configurations[Key] = UpdateDictionsary[Key]
    dump2file(FileName, Configurations)

#每两行加一行空格方便阅读
def addLineEvery2Lines(text):
    NewTextList = []
    AllLinesNumber = 0
    for Line in text.split('\n'):
        AllLinesNumber += 1
        NewTextList.append(Line)
        if AllLinesNumber % 2 == 0:
            NewTextList.append(' ')
    return '\n'.join(NewTextList)


