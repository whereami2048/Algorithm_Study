import sys
C, N = map(int, input().split())
marketings = [list(map(int, input().split())) for _ in range(N)]

dp = [sys.maxsize for _ in range(C + 100)]

dp[0] = 0

for cost, customers in marketings:
    for i in range(customers, C + 100):
        dp[i] = min(dp[i], dp[i - customers] + cost)

print(min(dp[C:]))