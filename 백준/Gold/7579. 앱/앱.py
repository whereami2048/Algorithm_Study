N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [[0 for _ in range(10001)] for _ in range(N+1)]

for i in range(1, N+1):
    for w in range(10001):
        if costs[i - 1] <= w:
            dp[i][w] = max(memories[i - 1] + dp[i - 1][w - costs[i - 1]], dp[i - 1][w])
        else:
            dp[i][w] = dp[i-1][w]

for i, c in enumerate(dp[-1]):
    if c >= M:
        print(i)
        break