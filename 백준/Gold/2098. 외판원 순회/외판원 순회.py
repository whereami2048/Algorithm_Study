import sys

N = int(sys.stdin.readline())
cost_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(1 << N - 1)] for _ in range(N)]


def dfs(i, route):
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1 << (N - 1)) - 1:
        if cost_arr[i][0]:
            return cost_arr[i][0]
        else:
            return float('inf')

    min_dist = float('inf')

    for j in range(1, N):
        if not cost_arr[i][j]:
            continue
        if route & (1 << j - 1):
            continue
        dist = cost_arr[i][j] + dfs(j, route | (1 << (j - 1)))
        min_dist = min(min_dist, dist)

    dp[i][route] = min_dist

    return min_dist


print(dfs(0, 0))