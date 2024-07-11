from collections import deque

n, k = map(int, input().split())

max_limit = 100001
time = [0] * max_limit
visited = [False for _ in range(max_limit)]

def bfs(x, end):
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()

        if x == end:
            return time[x]
        
        if -1 < x*2 < max_limit and visited[x*2] == 0:
            queue.appendleft(x*2)
            time[x*2] = time[x]
            visited[x*2] = True
            
        if -1 < x-1 < max_limit and visited[x-1] == 0:
            queue.append(x-1)
            time[x-1] = time[x]+1
            visited[x-1] = True
            
        if -1 < x+1 < max_limit and visited[x+1] == 0:
            queue.append(x+1)
            time[x+1] = time[x]+1
            visited[x+1] = True


print(bfs(n, k))