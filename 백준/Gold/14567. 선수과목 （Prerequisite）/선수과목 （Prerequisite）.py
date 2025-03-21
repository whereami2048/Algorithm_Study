from collections import deque

N, M = map(int, input().split())

constraints = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

for start, end in constraints:
    graph[start].append(end)
    indegree[end] += 1

queue = deque()

result = [1 for _ in range(N + 1)]

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()

    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

        result[next_node] = result[node] + 1



print(*result[1:])