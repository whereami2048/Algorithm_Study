import sys

input = sys.stdin.readline
n, space = map(int, input().split())
m = int(input())
box = [0] * (n + 1)
send = []
answer = 0
# 1. 도착하는 마을 마다 가장 빨리 도착하는 순서부터 최대로 담는다 - 틀림
# 2. [받는 마을, 보내는 마을] 순으로 정렬한다.
for i in range(m):
    a, b, amount = map(int, input().split())
    send.append([a, b, amount])
send.sort(key=lambda x: (x[1], x[0]))

for start, destination, boxes in send:
    maxbox = boxes
    # start부터 dest까지 얼만큼 박스를 보낼 수 있는지 검사
    for i in range(start, destination):
        maxbox = min(maxbox, space - box[i])
    # 박스를 담는 동시에 answer 또한 +, 어차피 담은 박스는 반드시 배달된다.
    for i in range(start, destination):
        box[i] += maxbox
    answer += maxbox
print(answer)