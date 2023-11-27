import sys

sys.setrecursionlimit(100000)

M, N, K = map(int, input().split())
rectangle = [list(map(int, input().split())) for _ in range(K)]

# M -> 세로
paper = [[False for _ in range(N)] for _ in range(M)]
visit = [[False for _ in range(N)] for _ in range(M)]
for rec in rectangle:
    lx = rec[0]
    ly = rec[1]
    rx = rec[2]
    ry = rec[3]
    for y in range(ly, ry):
        for x in range(lx, rx):
            paper[y][x] = True

area = 1
count = 0
areas = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(i, j):
    global area
    paper[i][j] = True
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x <= N - 1 and 0 <= y <= M - 1:
            if not paper[y][x]:
                area += 1
                dfs(y, x)


for i in range(M):
    for j in range(N):
        if not paper[i][j]:
            dfs(i, j)
            count += 1
            areas.append(area)
            area = 1

print(count)
print(" ".join(list(map(str, sorted(areas)))))


