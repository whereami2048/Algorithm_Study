import sys
input = sys.stdin.readline

n, s = map(int, input().split())

sequence = list(map(int, input().split()))

left_pos, right_pos = 0, 0
min_length = sys.maxsize
sum = 0

while True:
    if sum >= s:
        min_length = min(min_length, right_pos - left_pos)
        sum -= sequence[left_pos]
        left_pos += 1
    elif right_pos == n:
        break
    else:
        sum += sequence[right_pos]
        right_pos += 1

print(0 if min_length == sys.maxsize else min_length)

