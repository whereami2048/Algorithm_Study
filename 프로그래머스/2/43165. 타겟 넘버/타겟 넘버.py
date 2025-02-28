from collections import deque

def solution(numbers, target):
    answer = 0
    
    queue = deque()
    limit = len(numbers)
    queue.append((0, 0))
    
    while queue:
        cur_sum, cur_count = queue.popleft()
        
        if cur_count < limit:
            queue.append((cur_sum + numbers[cur_count], cur_count + 1))
            queue.append((cur_sum - numbers[cur_count], cur_count + 1))
        elif cur_count == limit:
            if cur_sum == target:
                answer += 1
    
    return answer