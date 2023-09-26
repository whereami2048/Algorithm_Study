def solution(n):
    answer = 0
    next = n+1
    format(n, 'b').count('1')
    while(format(n, 'b').count('1') != format(next, 'b').count('1')):
        next += 1
    
    return next