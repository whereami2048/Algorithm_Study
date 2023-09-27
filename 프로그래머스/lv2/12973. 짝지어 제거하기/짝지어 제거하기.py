def solution(s):
    if len(s) % 2 == 1: return 0 # 문자가 홀수개면 무조건 남는다.
    if len(s) == 2: # 문자가 2개이고, 같은 문자라면 무조건 가능
        return 1 if s[0] == s[1] else 0
            
    stack = [s[0]]
    
    for v in s[1:]:
        if len(stack) > 0 and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
            
    return 0 if len(stack) else 1

    return answer