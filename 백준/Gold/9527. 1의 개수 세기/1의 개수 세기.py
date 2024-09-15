import sys
import math

sys.setrecursionlimit(10 ** 8)

a, b = map(int, input().split())

def calculate(x):
    if x <= 0:
        return 0

    square = int(math.log2(x))
    under_pow = 2 ** square

    if under_pow == x:
        return square * x // 2 + 1

    diff = x - under_pow
    return calculate(under_pow) + diff + calculate(diff)


print(calculate(b) - calculate(a - 1))