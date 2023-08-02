N, K = map(int, input().split())

members = list(map(int, input().split()))

dif = []

for i in range(1, N):
    dif.append(members[i] - members[i-1])

dif.sort()
sum = 0

for i in range(N-K):
    sum += dif[i]

print(sum)