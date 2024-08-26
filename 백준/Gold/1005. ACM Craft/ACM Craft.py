import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    building_time = [0] + list(map(int, input().split()))
    building_order = {j: [] for j in range(1, n + 1)}
    degree = [0 for _ in range(n + 1)]

    for _ in range(k):
        x, y = map(int, input().split())
        building_order[x].append(y)
        degree[y] += 1

    target_building = int(input())

    dp = [0 for _ in range(n + 1)]
    queue = deque()

    for b in range(1, n + 1):
        if degree[b] == 0:
            dp[b] = building_time[b]
            queue.append(b)

    while queue:
        target = queue.popleft()

        for next in building_order[target]:
            degree[next] -= 1
            dp[next] = max(dp[target] + building_time[next], dp[next])

            if degree[next] == 0:
                queue.append(next)

    print(dp[target_building])
