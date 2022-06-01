#!/usr/bin/python3
for a in range(0, 100):

    if a < 99:
        print("0{}".format(a) if a < 10 else "{}".format(a), end=', ')

    else:
        print(a)
