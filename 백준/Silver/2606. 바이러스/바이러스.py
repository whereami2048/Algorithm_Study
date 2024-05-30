from collections import deque

computer_num = int(input())
pair_num = int(input())

if pair_num == 0:
    print(0)
    exit(0)
    
links = {i: [] for i in range(1, computer_num + 1)}
visited = [False] * (computer_num + 1)

for _ in range(pair_num):
    key, value = map(int, input().split())
    links[key].append(value)
    links[value].append(key)

count = 0


def bfs():
    queue = deque()
    queue.append(1)
    global count

    while queue:
        target = queue.popleft()
        for val in links[target]:
            if not visited[val]:
                visited[val] = True
                count += 1
                queue.append(val)

bfs()
print(count - 1)