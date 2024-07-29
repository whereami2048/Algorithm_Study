import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
candies = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootY] = rootX

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

friends_num = [1] * (n + 1)
dp = [0] * (k)

for i in range(1, n + 1):
    root = find(i)
    if root != i:
        candies[root] += candies[i]
        friends_num[root] += friends_num[i]

for i in range(1, n + 1):
    if i == parent[i]:
        for j in range(k - 1, friends_num[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - friends_num[i]] + candies[i])

print(max(dp))