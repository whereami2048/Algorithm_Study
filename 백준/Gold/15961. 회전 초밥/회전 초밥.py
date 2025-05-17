import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
answer = -1

dishes = [0] * (d + 1)
dishes[c] = 1
count = 1

# 초기 세팅
for i in range(k):
    if dishes[belt[i]] == 0:
        count += 1
    
    dishes[belt[i]] += 1

# sliding window
answer = count
for i in range(N):
    j = (i + k) % N

    if dishes[belt[j]] == 0:
        count += 1
    dishes[belt[j]] += 1

    if dishes[belt[i]] == 1:
        count -= 1
    dishes[belt[i]] -= 1

    answer = max(answer, count)

print(answer)
