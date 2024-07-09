import sys

input = sys.stdin.readline

v, e = map(int, input().split())

edges = []

for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(v + 1)]


def find_parent(parent, vertex):
    if parent[vertex] == vertex:
        return vertex

    parent[vertex] = find_parent(parent, parent[vertex])

    return parent[vertex]

def union_parent(x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

result = 0

for start, end, cost in edges:
    if not find_parent(parent, start) == find_parent(parent, end):
        union_parent(start, end)
        result += cost

print(result)