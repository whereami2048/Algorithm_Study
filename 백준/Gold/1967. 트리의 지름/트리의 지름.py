import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
     a, b, c = map(int, input().split())
     tree[a].append((b, c))
     tree[b].append((a, c))

visited = [-1] * (n + 1)
visited[1] = 0
def dfs(node, distance):
    for next_node, weight in tree[node]:
        if visited[next_node] == -1:
            visited[next_node] = distance + weight
            dfs(next_node, distance + weight)


dfs(1, 0)

max_idx, max_val = 0, 0
for i in range(1, len(visited)):
    if visited[i] > max_val:
        max_val = visited[i]
        max_idx = i

visited = [-1] * (n + 1)
visited[max_idx] = 0

dfs(max_idx, 0)

print(max(visited))
