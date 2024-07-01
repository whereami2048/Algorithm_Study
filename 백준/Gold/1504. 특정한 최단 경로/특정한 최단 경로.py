import sys
import heapq
input = sys.stdin.readline
N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

INF = sys.maxsize


def dijkstra(start_node, end_node):
    distance = [INF] * (N + 1)
    distance[start_node] = 0
    queue = []
    heapq.heappush(queue, (start_node, 0))

    while queue:
        current_node, dist = heapq.heappop(queue)

        if distance[current_node] < dist:
            continue

        for next_node, weight in graph[current_node]:
            if distance[next_node] > distance[current_node] + weight:
                distance[next_node] = distance[current_node] + weight
                heapq.heappush(queue, (next_node, distance[next_node]))

    return distance[end_node]


p1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
p2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if p1 >= INF and p2 >= INF:
    print(-1)
else:
    print(min(p1, p2))
