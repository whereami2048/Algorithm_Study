import sys
sys.setrecursionlimit(10000000)

t = int(input())

def dfs(x):
    visited[x] = True
    global count

    cycle.append(x)
    select_number = select_numbers[x]

    if visited[select_number]:
        if select_number in cycle:
            count += len(cycle[cycle.index(select_number):])
    else:
        dfs(select_number)


for i in range(t):
    n = int(input())
    select_numbers = [-1] + list(map(int, input().split()))

    visited = [False for _ in range(n + 1)]
    count = 0

    for j in range(1, n + 1):
        if not visited[j]:
            cycle = []
            dfs(j)

    print(n - count)
