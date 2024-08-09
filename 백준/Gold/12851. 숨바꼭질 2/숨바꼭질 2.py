from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.append(N)

dp = [0 for _ in range(100001)]

count, result = 0, 0

while queue:
    num = queue.popleft()
    temp = dp[num]

    if num == K:
        result = temp
        count += 1
        continue

    for i in [num - 1, num + 1, num * 2]:
        if 0 <= i < 100001 and (dp[i] == 0 or dp[i] == dp[num] + 1):
            dp[i] = dp[num] + 1
            queue.append(i)

print(result)
print(count)
