from collections import deque

def count_str(word, string):
    cnt = 0
    for i in range(len(word)):
        if word[i] == string[i]:
            cnt += 1
            
    return cnt

def bfs(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        s, step = queue.popleft()
        
        if s == target:
            return step
        
        for word in words:
            count = 0
            for i in range(len(s)):
                if s[i] != word[i]:
                    count += 1
                    
            if count == 1: 
                queue.append([word, step+1])
    

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    return bfs(begin, target, words)