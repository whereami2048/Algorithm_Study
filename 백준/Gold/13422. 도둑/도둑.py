T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    homes = list(map(int, input().split()))
    circle_homes = homes + homes[:M - 1]
    count = 1 if sum(circle_homes[:M]) < K else 0
    if N == M:
        print(count)
        continue
    sum_list = [0 for _ in range(N + M)]

    for i in range(N + M - 1):
        if i < M:
            sum_list[i] = sum_list[i-1] + circle_homes[i]
            continue

        sum_list[i] = sum_list[i-1] + circle_homes[i]
        if (sum_list[i] - sum_list[i-M]) < K:
            count += 1

    print(count)
