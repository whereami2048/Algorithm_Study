from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        target_num = queue.popleft()
        
        count = 0
        for q in queue:
            count += 1
            if target_num > q:
                break
        answer.append(count)
    return answer