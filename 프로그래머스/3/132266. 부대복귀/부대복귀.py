from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    costs = [-1 for _ in range(n + 1)]
    graph = {i: [] for i in range(n + 1)}
    
    for road in roads: 
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
    queue = deque([destination])
    costs[destination] = 0
    while queue:
        cur = queue.popleft()
        
        for next_node in graph[cur]:
            if costs[next_node] == -1:
                costs[next_node] = costs[cur] + 1
                queue.append(next_node)
    
    return [costs[source] for source in sources]