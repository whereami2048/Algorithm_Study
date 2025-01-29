N = int(input())
heights = list(map(int, input().split()))

answer = [-1 for _ in range(N)]

for i in range(N):
    count = -1
    for j in range(N):
        if answer[j] == -1:
            count += 1

        if count == heights[i]:
            answer[j] = i + 1
            break

print(*answer)