#!/usr/bin/python3
for a in range(1, 100):

    if a < 99:
        print(f'0{a:d}'if a < 10 else f'{a:d}', end=', ')

    else:
        print(f'{a:d}')
