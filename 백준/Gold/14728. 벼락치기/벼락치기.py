N, T = map(int, input().split())

chapters = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(T + 1):
        time = chapters[i][0]
        point = chapters[i][1]

        if j < time:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + point)

print(dp[N][T])

