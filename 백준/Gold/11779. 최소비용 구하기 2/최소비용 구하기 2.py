import heapq
import sys

INF = sys.maxsize

n = int(input())
m = int(input())

bus_info = {i: [] for i in range(n + 1)}

for _ in range(m):
    i, j, k = map(int, input().split())
    bus_info[i].append((j, k))

start, end = map(int, input().split())

distance = [INF for _ in range(n + 1)]

queue = []
cities = [0 for _ in range(n + 1)]

def dijkstra(start, end):
    distance[start] = 0
    heapq.heappush(queue, (start, distance[start]))

    while queue:
        cur_node, cur_distance, = heapq.heappop(queue)

        if distance[cur_node] < cur_distance:
            continue

        for next_node, next_distance in bus_info[cur_node]:
            if distance[next_node] > cur_distance + next_distance:
                distance[next_node] = cur_distance + next_distance
                cities[next_node] = cur_node
                heapq.heappush(queue, (next_node, distance[next_node]))


dijkstra(start, end)

road = [end]
now = end

while now != start:
    now = cities[now]
    road.append(now)

road.reverse()

print(distance[end])
print(len(road))
print(*road)
