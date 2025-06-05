N = int(input())
M = int(input())

vips = [int(input()) for _ in range(M)]

if N == 1:
    print(1)
    exit(0)
    
dp = [0 for _ in range(N + 1)]

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

count = 1
if M > 0:
    pos = 0
    for vip in vips:
        count *= dp[vip - pos - 1]
        pos = vip
    count *= dp[N - pos]
else:
    count = dp[N]

print(count)