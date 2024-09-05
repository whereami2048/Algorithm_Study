from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def open_door(keys, height, width):
  for i in range(height):
    for j in range(width):
      if building[i][j].lower() in keys:
        building[i][j] = '.'


def bfs():
  global count
  global visited
  queue = deque()
  queue.append((0, 0))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < height + 2 and 0 <= ny < width + 2:
        if not visited[nx][ny]:

          if temp_building[nx][ny].islower():
            keys.append(temp_building[nx][ny])
            temp_building[nx][ny] = '.'

            queue = deque()
            visited = [[False for _ in range(width + 2)] for _ in range(height + 2)]
            queue.append((nx, ny))

          elif temp_building[nx][ny] == '.':
            visited[nx][ny] = True
            queue.append((nx, ny))

          elif temp_building[nx][ny].isupper():
            if temp_building[nx][ny].lower() in keys:
              temp_building[nx][ny] = '.'
              queue.append((nx, ny))
              visited[nx][ny] = True


          elif temp_building[nx][ny] == '$':
            count += 1
            visited[nx][ny] = True
            temp_building[nx][ny] = '.'
            queue.append((nx, ny))

t = int(input())

for i in range(t):
  height, width = map(int, input().split())
  building = [list(input()) for _ in range(height)]
  keys = list(input())
  visited = [[False for _ in range(width + 2)] for _ in range(height + 2)]
  count = 0

  open_door(keys, height, width)

  temp_building = [['.' for _ in range(width + 2)] for _ in range(height + 2)]

  for x in range(height):
    for y in range(width):
      temp_building[x + 1][y + 1] = building[x][y]

  bfs()
  print(count)
