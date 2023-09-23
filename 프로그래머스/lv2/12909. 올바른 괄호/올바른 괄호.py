def solution(s):
    answer = True
    
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            if count > 0:
                count -= 1
        
    if count == 0:
        if s.count('(') < s.count(')'):
            return False
        else:            
            return True
    else:
        return False    