import sys

sys.setrecursionlimit(100000)

N = int(input())
rgb = [list(input()) for _ in range(N)]
not_visit = [[False for _ in range(N)] for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def not_dfs(i, j, color):
    not_visit[i][j] = True
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x <= N-1 and 0 <= y <= N-1:
            if not not_visit[x][y]:
                if rgb[x][y] == color:
                    not_dfs(x, y, color)

def dfs(i, j, color):
    visit[i][j] = True
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]

        if 0 <= x <= N-1 and 0 <= y <= N-1:
            if not visit[x][y]:
                if color == 'B':
                    if rgb[x][y] == color:
                        dfs(x, y, color)
                else:
                    if rgb[x][y] != 'B':
                        dfs(x, y, color)

not_count = 0
count = 0

for i in range(N):
    for j in range(N):
        if not not_visit[i][j]:
            not_dfs(i, j, rgb[i][j])
            not_count += 1

        if not visit[i][j]:
            dfs(i, j, rgb[i][j])
            count += 1

print(not_count, count)