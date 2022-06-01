#!/usr/bin/python3
for a in range(1, 100):

    if a == 99:
        print(a)

    else:
        print(f'0{a}' if a < 10 else f'{a}', end=', ')
