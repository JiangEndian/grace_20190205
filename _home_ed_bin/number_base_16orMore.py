#!/usr/bin/env python3

def times(n, base):
    string = "0123456789ABCDEF"
    if n < base:
        return string[n]
    else:
        return times(n // base, base) + string[n % base]

while True:
    print(times(int(input('n:')), int(input('base:'))))
