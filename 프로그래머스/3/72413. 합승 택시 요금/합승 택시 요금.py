import sys, heapq

def solution(n, s, a, b, fares):
    INF = sys.maxsize
    fee = {i: [] for i in range(n + 1)}
    
    for fare in fares:
        fee[fare[0]].append((fare[1], fare[2]))
        fee[fare[1]].append((fare[0], fare[2]))
    
    def dijkstra(start_node):
        distance = [INF for _ in range(n + 1)]
        distance[start_node] = 0
        queue = []
        heapq.heappush(queue, [start_node, 0])
        
        while queue:
            cur_node, cur_dist = heapq.heappop(queue)
            
            if distance[cur_node] < cur_dist:
                continue
                
            for next_node, next_dist in fee[cur_node]:    
                if cur_dist + next_dist < distance[next_node]:
                    distance[next_node] = cur_dist + next_dist
                    heapq.heappush(queue, [next_node, distance[next_node]])
        
        return distance
    
    result = [0]
    for i in range(1, n + 1):
        result.append(dijkstra(i))
            
    route = INF
    for i in range(1, n + 1):
        route = min(route, result[s][i] + result[i][a] + result[i][b])
        
    return route