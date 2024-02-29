import copy
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())

origin_map = [list(map(int, input().split())) for _ in range(n)]

answer = 0
def bfs():
    queue = deque()
    virus_map = copy.deepcopy(origin_map)

    for i in range(n):
        for j in range(m):
            if virus_map[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            dir_x = x + dx[i]
            dir_y = y + dy[i]

            if 0 <= dir_x < n and 0 <= dir_y < m:
                if virus_map[dir_x][dir_y] == 0:
                    virus_map[dir_x][dir_y] = 2
                    queue.append((dir_x, dir_y))

    global answer
    cnt = 0
    for i in range(n):
        for j in range(m):
            if virus_map[i][j] == 0:
                cnt += 1

    answer = max(answer, cnt)


def init_wall(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if origin_map[i][j] == 0:
                origin_map[i][j] = 1
                init_wall(count + 1)
                origin_map[i][j] = 0


init_wall(0)

print(answer)