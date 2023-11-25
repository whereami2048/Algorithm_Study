import sys

sys.setrecursionlimit(100000)

N, M, K = map(int, input().split())
foods = [list(map(int, input().split()))for _ in range(K)]

foods_map = [[False for _ in range(M)] for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

for k in range(K):
    for i in range(N):
        for j in range(M):
            if i == foods[k][0]-1 and j == foods[k][1]-1:
                foods_map[i][j] = True
                break

# M = 가로
count = 0

def dfs(y, x):
    global count
    if x + 1 <= M - 1:
        if not visit[y][x+1]:
            if foods_map[y][x+1]:
                visit[y][x+1] = True
                count += 1
                dfs(y, x+1)

    if x - 1 >= 0:
        if not visit[y][x-1]:
            if foods_map[y][x-1]:
                visit[y][x-1] = True
                count += 1
                dfs(y, x-1)

    if y + 1 <= N - 1:
        if not visit[y+1][x]:
            if foods_map[y+1][x]:
                visit[y+1][x] = True
                count += 1
                dfs(y+1, x)

    if y - 1 >= 0:
        if not visit[y-1][x]:
            if foods_map[y-1][x]:
                visit[y-1][x] = True
                count += 1
                dfs(y-1, x)

max_count = 0

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            if foods_map[i][j]:
                dfs(i, j)
                if count > max_count:
                    max_count = count

                count = 0

print(max_count)



