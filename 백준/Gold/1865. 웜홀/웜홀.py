import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellman_ford(n, roads):
    distance = [INF] * (n + 1)
    for i in range(n):
        for current_node, next_node, weight in roads:
            if distance[current_node] + weight < distance[next_node]:
                distance[next_node] = distance[current_node] + weight

                if i == n - 1:
                    return True

    return False


tc = int(input())

for _ in range(tc):
    N, M, W = map(int, input().split())
    roads = []

    for _ in range(M):
        s, e, t = map(int, input().split())
        roads.append((s, e, t))
        roads.append((e, s, t))

    for _ in range(W):
        s, e, t = map(int, input().split())
        roads.append((s, e, -t))

    if bellman_ford(N, roads):
        print("YES")
    else:
        print("NO")


