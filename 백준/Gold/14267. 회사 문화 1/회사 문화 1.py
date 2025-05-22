import sys
n, m = map(int, sys.stdin.readline().split())
grade = [0] + list(map(int, sys.stdin.readline().split()))
good = [0]*(n+1)

for _ in range(m):
    s,p = map(int, sys.stdin.readline().split())
    good[s] += p

for i in range(2, n+1):
    good[i] += good[grade[i]]

print(*good[1:])
