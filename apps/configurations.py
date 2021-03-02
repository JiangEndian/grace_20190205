#!/usr/bin/env python3

from MyPython3 import *


def readConfigurations(FileName):
    Configurations = {'InfoOfThisConfigurations':'This is a dictionsary to story configurations.'}
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


