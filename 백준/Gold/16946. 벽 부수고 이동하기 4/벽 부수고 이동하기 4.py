from collections import deque


def bfs(start, num):
    q = deque()
    q.append(start)

    count = 1
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = num
                count += 1
                q.append((nx, ny))

    return count


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

area = {}
area[0] = 0

num = 1
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0 and visited[x][y] == 0:
            visited[x][y] = num
            cnt = bfs((x, y), num)
            area[num] = cnt

            num += 1

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:

            ss = set()

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                    ss.add(visited[nx][ny])

            for s in ss:
                graph[x][y] += area[s]

            graph[x][y] %= 10

for i in graph:
    print("".join(map(str, i)))