def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            temp_str = s[i:j]
            
            if temp_str == temp_str[::-1]:
                answer = max(len(temp_str), answer)
    
    return answer