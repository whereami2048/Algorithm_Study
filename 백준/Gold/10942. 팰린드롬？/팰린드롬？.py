import sys

input = sys.stdin.readline

n = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))
m = int(input().rstrip())

dp = [[0 for _ in range(n)] for _ in range(n)]

for diff in range(n):
    for start in range(n - diff):
        end = start + diff

        if start == end:
            dp[start][end] = 1
        elif numbers[start] == numbers[end]:
            if end - start == 1:
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

for _ in range(m):
    s, e = map(int, input().rstrip().split())
    print(dp[s-1][e-1])
