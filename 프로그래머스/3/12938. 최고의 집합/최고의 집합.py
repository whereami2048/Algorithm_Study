def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    mod = s // n
    rest = s % n
    
    for _ in range(n):
        answer.append(mod)
    
    if rest != 0:
        for num in range(len(answer)):
            answer[num] += 1
            rest -= 1
            
            if rest == 0:
                break
    
    answer.sort()

    return answer