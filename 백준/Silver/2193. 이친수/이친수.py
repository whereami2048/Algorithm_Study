import sys

n = int(input())

if n == 1 or n == 2:
    print(1)
    sys.exit()

# [1인 개수, 0인 개수]
dp = [[0, 0] for _ in range(n+1)]
dp[1] = [1, 0]
dp[2] = [0, 1]
dp[3] = [1, 1]

for i in range(2, n + 1):
    dp[i] = [dp[i-1][1], dp[i-1][0] + dp[i-1][1]]

print(dp[n][0] + dp[n][1])