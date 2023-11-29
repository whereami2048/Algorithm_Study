import sys

sys.setrecursionlimit(10000)

N = int(input())

numbers = [-1]

for i in range(N):
    numbers.append(int(input()))


answer = set()


def dfs(i):
    if i == numbers[i]:
        answer.add(i)
        return

    if numbers[i] in up:
        up.add(i)
        down.add(numbers[i])
        return

    up.add(i)
    down.add(numbers[i])

    dfs(numbers[i])


for i in range(1, N+1):
    up = set()
    down = set()
    dfs(i)

    if len(up.difference(down)) == 0:
        answer = answer.union(up)

print(len(answer))
for num in sorted(list(answer)):
    print(num)