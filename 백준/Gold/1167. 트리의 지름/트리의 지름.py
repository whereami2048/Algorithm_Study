v = int(input())

vertex = {key: [] for key in range(1, v + 1)}

for i in range(v):
    input_string = list(map(int, input().split()))[:-1]
    key = input_string[0]
    for j in range(1, len(input_string), 2):
        vertex[key].append((input_string[j], input_string[j+1]))

visited = [-1] * (v + 1)
visited[1] = 0


def dfs(node, distance):
    for target_node, value in vertex[node]:
        if visited[target_node] == -1:
            visited[target_node] = distance + value
            dfs(target_node, distance + value)


dfs(1, 0)

max_idx, max_val = 0, 0
for i in range(1, len(visited)):
    if visited[i] > max_val:
        max_val = visited[i]
        max_idx = i

visited = [-1] * (v + 1)
visited[max_idx] = 0

dfs(max_idx, 0)

print(max(visited))