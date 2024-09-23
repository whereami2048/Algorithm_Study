import math, heapq

def solution(n, edge):
    answer = 0
    graph = {i: [] for i in range(1, n + 1)}
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    INF = math.inf
    distance = [INF for _ in range(n + 1)]
    
    def dijkstra(start_node):
        queue = []
        distance[start_node] = 0
        heapq.heappush(queue, [start_node, distance[start_node]])
        
        while queue:
            cur_node, cur_dist = heapq.heappop(queue)
            
            if cur_dist > distance[cur_node]:
                continue
            
            for next_node in graph[cur_node]:
                if distance[next_node] > cur_dist + 1:
                    distance[next_node] = cur_dist + 1
                    heapq.heappush(queue, [next_node, cur_dist + 1])
            
        
    dijkstra(1)
    distance = distance[1:]
    max_dist = max(distance)
    return distance.count(max_dist)