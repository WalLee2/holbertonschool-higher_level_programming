#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    if(length - 1 == 0):
        print('{:d} argument.'.format(length - 1))
    elif(length - 1 == 1):
        print('{:d} argument:\n{:d}: {:s}'
              .format((length - 1), (length - 1), sys.argv[1]))
    else:
        print('{:d} arguments:'.format(length - 1))
        for i in range(1, length):
            print('{:d}: {:s}'.format(i, sys.argv[i]))