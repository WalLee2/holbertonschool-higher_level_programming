#!/usr/bin/python3
for i in range (122, 96, -1):
    if(i % 2 == 0):
        print('{:.26}'.format(chr(i)), end="")
    else:
        i = chr(i - 32)
        print('{:.26}'.format(i), end="")
