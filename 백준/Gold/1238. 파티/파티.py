from sys import stdin
import heapq

input = stdin.readline

n, m, x = map(int, input().split())

toX = [[] for _ in range(n + 1)] 
toHome = [[] for _ in range(n + 1)] 
for _ in range(m):
      a, b, t = map(int, input().split())
      toX[a].append((b, t))
      toHome[b].append((a, t))

def dijk(graph, start):
      distance = [1e9] * (n + 1)
      q = []
      heapq.heappush(q, (0, start))
      distance[start] = 0
      while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                  continue
            for i in graph[now]:
                  cost = dist + i[1]
                  if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(q, (cost, i[0]))
      return distance[1:]

print(max([a+b for a, b in zip(dijk(toX, x), dijk(toHome, x))]))