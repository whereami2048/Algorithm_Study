# 10 <= P <= 50
# 0 <= N <= P
# 0 <= 모든 점수 <= 2000000000 (20억)

N, new_point, P = map(int, input().split())
ranking = []

if N :
    ranking = list(map(int, input().split()))

if N == 0:
    print(1)
else:
    if N == P and ranking[-1] >= new_point:
        print(-1)
    else:
        count = 1
        for i in range(N):
            if ranking[i] > new_point:
                count += 1

        print(count)