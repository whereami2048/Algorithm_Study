import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

g_boundary = []

for _ in range(P):
    g_boundary.append(int(input().rstrip()))

parent_gateway = [-1 for _ in range(G + 1)]


def find(pos):
    if parent_gateway[pos] < 0:
        return pos

    parent_gateway[pos] = find(parent_gateway[pos])

    return parent_gateway[pos]


def union(root_pos, target_pos):
    root_pos, target_pos = find(root_pos), find(target_pos)

    if root_pos == target_pos:
        return

    parent_gateway[target_pos] = root_pos


count = 0

for boundary in g_boundary:
    last_index = find(boundary)
    if last_index == 0:
        break

    union(last_index - 1, boundary)
    count += 1

print(count)
