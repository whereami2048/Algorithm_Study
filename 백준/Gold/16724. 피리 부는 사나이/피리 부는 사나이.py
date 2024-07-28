n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0
def dfs(x, y):
    global cnt

    visited[y][x] = True
    cycle.append((x, y))

    if graph[y][x] == 'U' and y > 0:
        y -= 1
    elif graph[y][x] == 'D' and y < n - 1:
        y += 1
    elif graph[y][x] == 'L' and x > 0:
        x -= 1
    elif graph[y][x] == 'R' and x < m - 1:
        x += 1

    if visited[y][x]:
        if (x, y) in cycle:
            cnt += 1
    else:
        dfs(x, y)


for y in range(n):
    for x in range(m):
        cycle = []
        dfs(x, y)

print(cnt)