import sys
input = sys.stdin.readline
INF = sys.maxsize
result = INF

n = int(input())

rgb = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][i] = rgb[0][i]

    for j in range(1, n):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    for k in range(3):
        if k != i:
            result = min(result, dp[-1][k])

print(result)