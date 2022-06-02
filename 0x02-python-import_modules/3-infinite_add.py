#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":

    i = len(argv)

    if i <= 2:
        print("0")

    elif i > 2:
        n = 1
        result = 0
        while n < i:
            result += int(argv[i - n])
            n += 1
        print(result)
