import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())
arr = [list(input()) for _ in range(m)]
psum = [[[0, 0, 0] for _ in range(n+1)] for _ in range(m+1)]

for x in range(m):
    for y in range(n):
        for z in range(3):
            psum[x+1][y+1][z] = psum[x+1][y][z] + \
                psum[x][y+1][z] - psum[x][y][z]
        if arr[x][y] == "J":
            psum[x+1][y+1][0] += 1
        elif arr[x][y] == "O":
            psum[x+1][y+1][1] += 1
        elif arr[x][y] == "I":
            psum[x+1][y+1][2] += 1
for _ in range(k):
    result = [0, 0, 0]
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(3):
        result[i] = psum[x2][y2][i] - psum[x1-1][y2][i] - \
            psum[x2][y1-1][i] + psum[x1-1][y1-1][i]
    print(result[0], result[1], result[2])