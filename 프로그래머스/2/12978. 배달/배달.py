import heapq, sys

def solution(N, road, K):
    answer = 0
    INF = sys.maxsize
    road_map = {i: [] for i in range(1, N + 1)}
    
    for a, b, c in road:
        road_map[a].append((b, c))
        road_map[b].append((a, c))
    
    def dijkstra(node):
        distance = [INF for i in range(N + 1)]
        queue = []
        distance[node] = 0
        heapq.heappush(queue, (node, distance[node]))
        
        while queue:
            cur_node, cur_distance = heapq.heappop(queue)
            
            if distance[cur_node] < cur_distance:
                continue
                
            for new_node, new_distance in road_map[cur_node]:
                next_distance = cur_distance + new_distance
                
                if next_distance < distance[new_node]:
                    distance[new_node] = next_distance
                    heapq.heappush(queue, (new_node, next_distance))
        
        return distance
    
    distances = dijkstra(1)
    distances = list(filter(lambda x: x <= K, distances))
    return len(distances)