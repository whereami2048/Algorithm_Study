N, M = map(int, input().split())

friends = {i: [] for i in range(N)}

for _ in range(M):
  a, b = map(int, input().split())
  friends[a].append(b)
  friends[b].append(a)

visited = [False] * N

answer = 0
def dfs(start, depth):
  global answer
  visited[start] = True

  if depth == 5:
    answer = 1
    return

  for i in friends[start]:
    if not visited[i]:
      dfs(i, depth + 1)

  visited[start] = False

for i in range(N):
  dfs(i, 1)

print(answer)
