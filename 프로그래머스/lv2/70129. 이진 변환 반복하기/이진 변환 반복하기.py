def solution(s):
    answer = []
    count = 0
    zero = 0
    
    
    print(s)
    while(s != '1'):
        zero += s.count('0')
        s = s.replace('0', '')
        s = format(len(s), 'b')
        count += 1
    
    answer.append(count)
    answer.append(zero)
    return answer