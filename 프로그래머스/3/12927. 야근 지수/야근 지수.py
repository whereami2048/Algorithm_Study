import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    
    arr = [-w for w in works]
    heapq.heapify(arr)
    
    for _ in range(n):
        i = heapq.heappop(arr)
        i += 1
        heapq.heappush(arr, i)
    
    return sum([a ** 2 for a in arr])
