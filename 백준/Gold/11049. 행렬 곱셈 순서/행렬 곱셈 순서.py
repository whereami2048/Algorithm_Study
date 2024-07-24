import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
processions = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

for diff in range(1, n):
    for start in range(n):
        end = start + diff

        if end >= n:
            break

        dp[start][end] = 2 ** 31

        for percent in range(start, end):
            dp[start][end] = min(dp[start][end],
                                        dp[start][percent] +
                                        dp[percent + 1][end] +
                                        processions[start][0] *
                                        processions[percent][1] *
                                        processions[end][1])

print(dp[0][-1])
