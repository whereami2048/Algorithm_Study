import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))

result = sys.maxsize
house = []
chicken_house = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken_house.append([i, j])

for chicken in combinations(chicken_house, m):
    chicken_total = 0

    for h in house:
        chicken_distance = sys.maxsize

        for j in range(m):
            chicken_distance = min(chicken_distance, abs(h[0] - chicken[j][0]) + abs(h[1] - chicken[j][1]))

        chicken_total += chicken_distance
    result = min(result, chicken_total)

print(result)