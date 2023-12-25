n, k = map(int, input().split())

nap = []
nap.append([0, 0])
for _ in range(n):
    nap.append(list(map(int, input().split())))

# nap[0] = w, nap[1] = v

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = nap[i][0], nap[i][1]
        if w <= j:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
