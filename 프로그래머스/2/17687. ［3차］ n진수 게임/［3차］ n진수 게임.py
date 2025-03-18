def change_formation(formation, num):
    result = ''
    
    while num != 0:
        add_num = num % formation
        
        if add_num >= 10:
            add_num = chr(65 + add_num - 10)
            
        result = str(add_num) + result
        num = num // formation
    
    return result if result != '' else '0'

def solution(n, t, m, p):
    answer = ''
    result = ''
    
    for i in range(m*t):
        result += change_formation(n, i)
    
    while len(answer) < t:
        answer += result[p-1]
        p += m
        
    return answer