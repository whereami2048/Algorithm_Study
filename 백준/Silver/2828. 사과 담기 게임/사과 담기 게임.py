N, M = map(int, input().split())
J = int(input())
pos = []
box_left = 1
width = M - 1
box_right = box_left + width
answer = 0
for i in range(J):
    pos.append(int(input()))

for i in range(len(pos)):
    if box_right <= pos[i]:
        answer += pos[i] - box_right
        box_right = pos[i]
        box_left = box_right - width
    elif pos[i] <= box_left:
        answer += box_left - pos[i]
        box_left = pos[i]
        box_right = box_left + width

print(answer)


