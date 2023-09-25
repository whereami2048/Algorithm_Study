def solution(n):
    answer = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if (j-i+1)*(i+j)/2 == n:
                answer += 1
                break
            elif (j-i+1)*(i+j)/2 > n:
                break
    return answer