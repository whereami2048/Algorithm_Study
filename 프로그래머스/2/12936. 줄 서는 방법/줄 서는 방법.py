import math

def solution(n, k):
    arr = [i for i in range(1, n + 1)]
    answer = []
    while arr:
        mod = math.factorial(n - 1)
        answer.append(arr.pop((k - 1) // mod))

        k %= mod
        n -= 1
    
    return answer