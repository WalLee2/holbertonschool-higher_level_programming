#!/usr/bin/python3
def pow(a, b):
    if (b != abs(b)):
        return('{:.4f}'.format(a**b))
    else:
        return('{:d}'.format(a ** b))
