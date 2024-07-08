n, m = map(int, input().split())

result = []


def dfs(pos):
    if len(result) == m:
        print(*result)
        return

    for i in range(pos, n + 1):
        result.append(i)
        dfs(i)
        result.pop()


dfs(1)

