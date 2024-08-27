from collections import deque


n, m = map(int, input().split())

in_degree = [0 for _ in range(n + 1)]
relation = [[] for _ in range(n + 1)]

for i in range(m):
    input_str = list(map(int, input().split()))[1:]

    for j in range(len(input_str) - 1):
        in_degree[input_str[j + 1]] += 1
        relation[input_str[j]].append(input_str[j + 1])

queue = deque()

order = []

for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)
        order.append(i)

while queue:
    num = queue.popleft()
    for j in relation[num]:
        in_degree[j] -= 1

        if in_degree[j] == 0:
            queue.append(j)
            order.append(j)

if len(order) != n:
    print(0)
else:
    for i in range(n):
        print(order[i])
        