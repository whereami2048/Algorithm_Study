import sys
INF = sys.maxsize

n = int(input())
m = int(input())

bus_info = []
distance = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    bus_info.append(tuple(map(int, input().split())))

for start, end, cost in bus_info:
    if start == end:
        distance[start][end] = 0
        continue

    distance[start][end] = min(cost, distance[start][end])



for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                distance[i][j] = 0
                continue
                
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, n + 1):
    dis = distance[i]
    for j in range(1, n + 1):
        if dis[j] == INF:
            print(0, end=' ')
        else:
            print(dis[j], end=' ')
    print()