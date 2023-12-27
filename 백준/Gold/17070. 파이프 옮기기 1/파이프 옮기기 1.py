n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# 0: 옆, 1: 위, 2: 대각
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

dp[0][0][1] = 1

for i in range(2, n) :
    if data[0][i] == 0 :
        dp[0][0][i] = dp[0][0][i-1]

for x in range(1, n) :
    for y in range(1, n) :
        # 대각
        if data[x][y] == 0 and data[x-1][y] == 0 and data[x][y-1] == 0 :
            dp[2][x][y] = dp[0][x-1][y-1] + dp[1][x-1][y-1] + dp[2][x-1][y-1]

        if data[x][y] == 0 :
            # 옆
            dp[0][x][y] = dp[0][x][y-1] + dp[2][x][y-1]
            # 
            dp[1][x][y] = dp[1][x-1][y] + dp[2][x-1][y]

print(sum(dp[i][n-1][n-1] for i in range(3)))
 