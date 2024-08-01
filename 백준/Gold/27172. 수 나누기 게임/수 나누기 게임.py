import sys

input = sys.stdin.readline
n = int(input())

players = []
answer = dict()
maxNum = 0

for i, num in enumerate([*map(int, input().rstrip().split())]):
    maxNum = max(maxNum, num)
    players.append((i, num))
    answer[num] = 0

players.sort(key=lambda x: x[1])

for i in range(n):

    _, num = players[i]

    for target in range(num * 2, maxNum + 1, num):
        if target in answer:
            answer[num] += 1
            answer[target] -= 1

for key, item in answer.items():
    print(item, end=" ")