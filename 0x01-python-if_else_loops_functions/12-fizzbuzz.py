#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:
            result = "FizzBuzz"

        elif a % 3 == 0:
            result = "Fizz"

        elif a % 5 == 0:
            result = "Buzz"

        else:
            result = a

        print(result, end=' ')

