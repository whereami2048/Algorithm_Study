import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

bus_fee = [[] for _ in range(n + 1)]

for i in range(m):
    start, end, weight = map(int, input().split())
    bus_fee[start].append((end, weight))

start_city, end_city = map(int, input().split())


def dijkstra(start_city):
    distance = [INF] * (n + 1)
    queue = []
    distance[start_city] = 0
    heapq.heappush(queue, (0, start_city))

    while queue:
        current_dist, current_city = heapq.heappop(queue)

        if current_dist > distance[current_city]:
            continue

        for new_city, new_dist in bus_fee[current_city]:
            if new_dist + current_dist < distance[new_city]:
                distance[new_city] = new_dist + current_dist
                heapq.heappush(queue, (new_dist + current_dist, new_city))

    return distance


result_distance = dijkstra(start_city)

print(result_distance[end_city])
