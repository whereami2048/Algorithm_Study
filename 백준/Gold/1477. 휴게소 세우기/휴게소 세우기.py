N, M, L = map(int, input().split())

buildings = [0] + list(map(int, input().split())) + [L]
buildings.sort()

left = 1
right = L - 1
answer = 0

while left <= right:
    count = 0
    mid = (left + right) // 2

    for i in range(1, len(buildings)):
        if buildings[i] - buildings[i - 1] > mid:
            count += (buildings[i] - buildings[i - 1] - 1) // mid

    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)