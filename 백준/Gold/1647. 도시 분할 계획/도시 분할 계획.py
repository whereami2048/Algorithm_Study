import sys
input = sys.stdin.readline

n, m = map(int, input().split())

roads = []

for i in range(m):
    a, b, c = map(int, input().split())
    roads.append((a, b, c))

roads.sort(key=lambda x: x[2])
parent = [i for i in range(n + 1)]


def find(pos):
    if parent[pos] != pos:
        parent[pos] = find(parent[pos])

    return parent[pos]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


sum_weight = 0
last_weight = 0

for a, b, c in roads:
    if find(a) != find(b):
        union(a, b)
        sum_weight += c
        last_weight = c

print(sum_weight - last_weight)