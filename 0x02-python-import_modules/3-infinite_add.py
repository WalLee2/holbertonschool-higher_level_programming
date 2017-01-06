#!/usr/bin/python3
import sys
length = len(sys.argv)
num = 0
for i in range(1, length):
    num += int(sys.argv[i])
print('{:d}'.format(num))
