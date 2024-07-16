import sys
input = sys.stdin.readline

n, m = map(int, input().split())

history = []

for i in range(m):
    history.append(tuple(map(int, input().split())))

parents = [i for i in range(n)]
cnt = 0

def find(pos):
    if parents[pos] != pos:
        parents[pos] = find(parents[pos])

    return parents[pos]


for index, (a, b) in enumerate(history):
    x = find(a)
    y = find(b)
    if x < y:
        parents[y] = x
    elif x > y:
        parents[x] = y
    else:
        cnt = index + 1
        break

print(cnt)
