#!/usr/bin/python3
def uppercase(str):
    for u in str:
        if ord(u) >= 97 and ord(u) <= 122:
            upper = ord(u) - 32
        else:
            upper = ord(u)
        print("{}".format(chr(upper)), end='')
    print("")
