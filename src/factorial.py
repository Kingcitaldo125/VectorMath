import math


def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

fact1 = factorial(52)
print(fact1,sep=",")