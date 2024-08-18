import heapq
n = int(input())

university = [tuple(map(int, input().split())) for _ in range(n)]
university.sort(key=lambda x: (x[1], -x[0]))

total_cost = 0
pos = 1
queue = []
for univ in university:
    cost, limit = univ
    heapq.heappush(queue, cost)

    if limit < len(queue):
        heapq.heappop(queue)

print(sum(queue))