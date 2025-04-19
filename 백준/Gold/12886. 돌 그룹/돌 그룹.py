from collections import deque

A, B, C = map(int, input().split())

total = A + B + C
if total % 3 != 0:
  print(0)
  exit(0)

visited = [[False] * total for _ in range(total)]

queue = deque([(A, B)])
visited[A][B] = True

while queue:
  a, b = queue.popleft()
  c = total - (a + b)

  if a == b == c:
    print(1)
    exit(0)

  for x, y in [(a, b), (b, c), (a, c)]:
    if x == y:
      continue

    if x > y:
      x, y = y, x

    x, y = x + x, y - x
    min_val = min(x, y, total - (x + y))
    max_val = max(x, y, total - (x + y))

    if visited[min_val][max_val]:
      continue

    queue.append((min_val, max_val))
    visited[min_val][max_val] = True

print(0)

