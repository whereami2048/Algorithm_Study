import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))  # v1에서 v2로 w거리

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])