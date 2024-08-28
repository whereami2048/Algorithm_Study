import heapq

n, m = map(int, input().split())

solving_order = [[] for _ in range(n + 1)]
in_degree = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    solving_order[x].append(y)
    in_degree[y] += 1

queue = []
result = []

for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    target = heapq.heappop(queue)
    result.append(target)

    for num in solving_order[target]:
        in_degree[num] -= 1

        if in_degree[num] == 0:
            heapq.heappush(queue, num)

print(*result)