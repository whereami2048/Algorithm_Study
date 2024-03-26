N, K = int(input()), int(input())

start, end = 1, K

answer = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(1, N + 1):
        count += min(mid // i, N)

    if count >= K:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1


print(answer)