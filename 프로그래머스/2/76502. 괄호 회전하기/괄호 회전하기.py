from collections import deque


# 문자열을 deque로 받아 deque를 rotate 시킴
def solution(s):  
    count = 0
    deq = deque()
    for i in s:
        deq.append(i)
    
    for _ in range(len(s)):
        if check(deq) == True:
            count += 1
        deq.rotate(-1)
    
    return count
    

# deque 내 괄호의 짝이 맞는지를 확인하는 함수
def check(s):
    chk = []
    for i in s:
        chk.append(i)
        if len(chk)>=2:
            if(chk[-1] == ']' and chk[-2] == '['):
                chk.pop()
                chk.pop()
            elif(chk[-1] == ')' and chk[-2] == '('):
                chk.pop()
                chk.pop()
            elif(chk[-1] == '}' and chk[-2] == '{'):
                chk.pop()
                chk.pop()
    
    if chk:
        return False
    else:
        return True