import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and cheese[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                elif cheese[nx][ny] == 1:
                    visited[nx][ny] = visited[nx][ny] + 1


n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

epoch = 0

while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]

    bfs(0, 0)
    epoch += 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                cheese[i][j] = 0

    block_cnt = 0
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 0:
                block_cnt += 1

    if block_cnt == (n * m):
        break

print(epoch)