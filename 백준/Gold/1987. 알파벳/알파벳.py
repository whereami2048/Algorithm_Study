import sys

sys.setrecursionlimit(10000)

R, C = map(int, input().split())

alpha = [list(input()) for _ in range(R)]

count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

record = set()


def dfs(j, i, cnt):
    global count
    cnt += 1

    count = max(count, cnt)

    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x <= C - 1 and 0 <= y <= R - 1:
            if alpha[y][x] not in record:
                record.add(alpha[y][x])
                dfs(y, x, cnt)
                record.remove(alpha[y][x])


record.add(alpha[0][0])
dfs(0, 0, count)

print(count)
