import heapq
from math import inf

def solution(stones, k):
    answer = inf
    size = len(stones)
    
    queue = []
    
    for i in range(k - 1):
        heapq.heappush(queue, [-stones[i], i])
        
    for i in range(k - 1, size):
        heapq.heappush(queue, [-stones[i], i])
        
        while queue[0][1] < i - k + 1:
            heapq.heappop(queue)
            
        answer = min(answer, -queue[0][0]) 

    return answer