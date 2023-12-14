import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

dp = [0] * n
dp[0] = m[0]

for i in range(1, n):
    for j in range(i):
        if m[i] > m[j]:
            dp[i] = max(dp[i], dp[j] + m[i])
        else:
            dp[i] = max(dp[i], m[i])

print(max(dp))