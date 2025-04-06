from collections import deque
N, M = map(int, input().split())

bridges = {i:[] for i in range(1, N + 1)}

for i in range(M):
    start, right, weight = map(int, input().split())
    bridges[start].append((right, weight))
    bridges[right].append((start, weight))

fac1, fac2 = map(int, input().split())

def bfs(weight):
    queue = deque()
    queue.append(fac1)
    visited = [False] * (N + 1)
    visited[fac1] = True

    while queue:
        node = queue.popleft()

        for index, w in bridges[node]:
            if not visited[index] and w >= weight:
                visited[index] = True
                queue.append(index)

    if visited[fac2]:
        return True

    return False

left, right = 1, 1000000000

answer = 0
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)