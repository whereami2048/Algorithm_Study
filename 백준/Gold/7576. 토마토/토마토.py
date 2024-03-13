import sys
from collections import deque

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]

queue = deque()

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            queue.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    while queue:
        (pos_x, pos_y) = queue.popleft()

        for i in range(4):
            x = pos_x + dx[i]
            y = pos_y + dy[i]

            if 0 <= x < N and 0 <= y < M and tomatos[x][y] == 0:
                tomatos[x][y] = tomatos[pos_x][pos_y] + 1
                queue.append((x, y))


bfs()

for arr in tomatos:
    if 0 in arr:
        print(-1)
        sys.exit()

max_int = 0
for arr in tomatos:
    max_int = max(max(arr), max_int)

print(max_int - 1)
