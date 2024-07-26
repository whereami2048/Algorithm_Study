import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]

for _ in range(m):
    before, after = map(int, input().split())
    graph[before].append(after)
    degree[after] += 1

queue = deque()

for i in range(1, n + 1):
    if degree[i] == 0:
        queue.append(i)

answer = []

while queue:
    num = queue.popleft()
    answer.append(num)

    for i in graph[num]:
        degree[i] -= 1

        if degree[i] == 0:
            queue.append(i)

print(*answer)


