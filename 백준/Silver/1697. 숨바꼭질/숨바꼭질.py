from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return count[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < 100001 and not count[next_v]:
                count[next_v] = count[v] + 1
                q.append(next_v)

n, k = map(int, input().split())
count = [0] * 100001
print(bfs(n))