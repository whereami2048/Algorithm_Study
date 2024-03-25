N, K, D = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(K)]

start, end = 1, N
res = 0

answer = 0

def count_dotori(target):
    count = 0
    for s, e, inter, in rules:
        e = min(target, e)
        if s <= min(target, e):
            count += (e - s) // inter + 1

    return count


while start <= end:
    mid = (start + end) // 2
    if count_dotori(mid) < D:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1


print(answer)
