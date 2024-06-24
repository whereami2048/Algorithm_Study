def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    a, b = 0, 0
    size = len(A)
    
    while size != 0:
        if A[a] < B[b]:
            answer += 1
            b += 1
        a += 1
        size -= 1
    
    return answer

