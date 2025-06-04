N, S, M = map(int, input().split())

volumes = list(map(int, input().split()))

dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

dp[0][S] = True

for i in range(1, N + 1):
    for j in range(M + 1):
        target_volume = volumes[i - 1]
        if dp[i-1][j]:
            if 0 <= j - target_volume <= M:
                dp[i][j - target_volume] = True

            if 0 <= j + target_volume <= M:
                dp[i][j + target_volume] = True

answer = -1

for i in range(M + 1):
    if dp[N][i]:
        answer = max(answer, i)

print(answer)