n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

dp = [[1 for _ in range(m)] for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = graph[i][j]
        elif graph[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

answer = max(map(max, dp))
print(answer**2)
