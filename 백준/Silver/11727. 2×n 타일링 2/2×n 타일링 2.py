import sys

# dp[1] = 1
# 2/1
# dp[2] = 3
# 2/2
# 2/1 X 2
# 1/2 X 2
# dp[3] =

n = int(input())

if n == 1:
    print(1)
    sys.exit()

dp = [ 0 for _ in range(n+1)]

dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n] % 10007)
