n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]
points.append(points[0])

answer = 0

for i in range(n):
    answer += points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1]

print(abs(answer) / 2)
