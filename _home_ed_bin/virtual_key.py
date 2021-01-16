#!/usr/bin/env python3

import virtkey

import time

v = virtkey.virtkey()

KEY = input('inputAKey:')

#time.sleep(3)

#v.press_keysym(65507) #Ctrl键位

v.press_unicode(ord(KEY))
v.release_unicode(ord(KEY))

#v.release_keysym(65507) #Ctrl键位

