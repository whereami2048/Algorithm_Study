import heapq
from math import inf

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    distance = [inf] * (n + 1)
    queue = []
    
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(queue, [0, gate])

    while queue:
        d, i = heapq.heappop(queue)

        if distance[i] < d or i in summits:
            continue
            
        for j, dd in graph[i]:
            dd = max(distance[i], dd)
            if distance[j] > dd:
                distance[j] = dd
                heapq.heappush(queue, [dd, j])

    answer = [-1, inf]
    for summit in sorted(summits):
        if distance[summit] < answer[1]:
            answer[0] = summit
            answer[1] = distance[summit]
            
    return answer