import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input()[:-1])) for _ in range(n)]

history = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))
    history[x][y][0] = 1

    while queue:
        x, y, cnt, = queue.popleft()

        if x == m-1 and y == n-1:
            return history[y][x][cnt]

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue

            if maze[next_y][next_x] == 1 and cnt == 0:
                history[next_y][next_x][1] = history[y][x][0] + 1
                queue.append((next_x, next_y, 1))

            if maze[next_y][next_x] == 0 and history[next_y][next_x][cnt] == 0:
                history[next_y][next_x][cnt] = history[y][x][cnt] + 1
                queue.append((next_x, next_y, cnt))

    return -1

print(bfs(0, 0))