N, C = map(int, input().split())

home = [int(input()) for _ in range(N)]
home.sort()

start = 1
end = home[-1] - home[0]

answer = 0

while(start <= end):
    count = 1
    center = (start + end) // 2
    pos = home[0]

    for i in range(1, N):
        if home[i] >= pos + center:
            count += 1
            pos = home[i]

    if count >= C:
        start = center + 1
        answer = center
    else:
        end = center - 1


print(answer)