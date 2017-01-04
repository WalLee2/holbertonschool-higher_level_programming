#!/usr/bin/python3
for i in range(0, 10):
    for a in range(0, 10):
        if(i < a and not (i == 8 and a == 9)):
            print('{:d}{:d}, '.format(i, a), end="")
print('{:d}'.format(89))
