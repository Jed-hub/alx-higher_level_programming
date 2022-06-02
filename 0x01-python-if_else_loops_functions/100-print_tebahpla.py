#!/usr/bin/python3
for i in range(-90, -64):
    print("{}".format(chr(-i + 32)) if i % 2 == 0 else "{}".format(chr(-i)), end='')
