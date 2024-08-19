n = int(input())
children = list(map(int, input().split()))

index = [-1 for _ in range(n + 1)]

for idx, value in enumerate(children):
    index[value] = idx

cnt = 1
max_len = 1

for i in range(1, n):
    if index[i] < index[i + 1]:
        cnt += 1
    else:
        max_len = max(max_len, cnt)
        cnt = 1

print(n - max_len if n != 1 else 0)
