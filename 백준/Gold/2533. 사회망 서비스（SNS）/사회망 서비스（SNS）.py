import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

arr = [[] for _ in range(n + 1)]
for u, v in edges:
    arr[u].append(v)
    arr[v].append(u)

dp = [[0, 0] for _ in range(n + 1)]

visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    dp[node][1] = 1  # 현재 노드를 얼리 어답터로 선택한 경우

    for neighbor in arr[node]:
        if not visited[neighbor]:
            dfs(neighbor)
            dp[node][0] += dp[neighbor][1]  # 현재 노드를 얼리 어답터가 아닐 때
            dp[node][1] += min(dp[neighbor][0], dp[neighbor][1])  # 현재 노드를 얼리 어답터일 때

dfs(1)

print(min(dp[1][0], dp[1][1]))
                