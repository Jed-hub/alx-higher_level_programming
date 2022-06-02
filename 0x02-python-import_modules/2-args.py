#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = len(argv)

    if i == 1:
        print("0 arguments.")

    elif i == 2:
        print(i - 1, "argument:")
        print("1:", argv[i - 1])

    else:
        print(i - 1, "arguments:")

        n = 1

        while n < i:
            print("{}:".format(n), argv[n])
            n += 1
