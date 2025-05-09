line_count = int(input())

lines = []

for _ in range(line_count):
    lines.append(list(map(int, input().split())))

lines.sort()

dp = [1] * line_count

for i in range(1, line_count):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(line_count - max(dp))