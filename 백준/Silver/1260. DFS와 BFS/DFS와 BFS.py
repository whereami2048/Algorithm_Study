from collections import deque

n, m, v = map(int, input().split())
trunks = {(i + 1): [] for i in range(n)}

for _ in range(m):
    key, value = map(int, input().split())
    trunks[key].append(value)
    trunks[value].append(key)

for key in trunks.keys():
    trunks[key] = sorted(trunks[key])

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
visited_node_dfs = []
visited_node_bfs = []

def dfs(node):
    visited_dfs[node] = True
    if trunks.get(node):
        values = trunks[node]
    else:
        values = []

    for value in values:
        if not visited_dfs[value]:
            visited_node_dfs.append(value)
            dfs(value)

def bfs(node):
    temp_nodes = deque([node])
    visited_bfs[node] = True

    while temp_nodes:
        target_node = temp_nodes.popleft()

        print(target_node, end=' ')

        temp_node_list = trunks[target_node]

        for candidate_node in temp_node_list:
            if not visited_bfs[candidate_node]:
                temp_nodes.append(candidate_node)
                visited_bfs[candidate_node] = True


visited_node_dfs.append(v)
dfs(v)
for val in visited_node_dfs:
    print(val, end=' ')
print()
bfs(v)
