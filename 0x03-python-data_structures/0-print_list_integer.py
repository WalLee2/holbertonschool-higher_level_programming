#/usr/bin/python3
def print_list_integer(list=[]):
    for i in range (len(list)):
        i += 48
        print(str.format(chr(i)))
