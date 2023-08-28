import heapq

T = int(input())

files = []

for i in range(T):
    num = int(input())
    files = list(map(int, input().split()))
    cnt = 0
    heapq.heapify(files)
    while len(files) > 1:
        num1 = heapq.heappop(files)
        num2 = heapq.heappop(files)
        cnt += num1 + num2
        heapq.heappush(files, num1 + num2)

    print(cnt)


