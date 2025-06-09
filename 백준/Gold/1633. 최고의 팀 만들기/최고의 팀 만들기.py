players = []

while True:
    try:
        white, black = map(int, input().split())
        players.append((black, white))
    except:
        break

size = len(players)

dp = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(size + 1)]

for i in range(size):
    for b in range(16):
        for w in range(16):
            if b < 15:
                dp[i+1][b+1][w] = max(dp[i+1][b+1][w], dp[i][b][w] + players[i][1])
            if w < 15:
                dp[i + 1][b][w + 1] = max(dp[i + 1][b][w + 1], dp[i][b][w] + players[i][0])

            dp[i + 1][b][w] = max(dp[i + 1][b][w], dp[i][b][w])

print(dp[size][15][15])
