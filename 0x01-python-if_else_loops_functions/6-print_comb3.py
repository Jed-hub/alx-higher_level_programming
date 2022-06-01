#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1, 10):

        if b > a:
            if a != 8 or b != 9:
                print("{0}{1}".format(a, b), end=', ')
            else:
                print("{0}{1}".format(a, b))
