def solution(n):
    pres, next = 1, 2
    if n == 1:
        return 1
    for i in range(2,n):
        pres, next = next, pres+next
    return next % 1234567