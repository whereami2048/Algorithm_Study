import sys
input = sys.stdin.readline
n = int(input())

arr = [[] for _ in range(4)]

for i in range(n):
    input_arr = list(map(int, input().split()))
    for j in range(4):
        arr[j].append(input_arr[j])

ab, cd = [], []

for i in range(n):
    for j in range(n):
        ab.append(arr[0][i] + arr[1][j])
        cd.append(arr[2][i] + arr[3][j])

ab.sort()
cd.sort()

left_pos = 0
right_pos = n**2 - 1
count = 0

while left_pos < n**2 and right_pos >= 0:
    if ab[left_pos] + cd[right_pos] == 0:
        temp_left_pos, temp_right_pos = left_pos + 1, right_pos - 1

        while temp_left_pos < n**2 and ab[temp_left_pos] == ab[left_pos]:
            temp_left_pos += 1

        while temp_right_pos >= 0 and cd[temp_right_pos] == cd[right_pos]:
            temp_right_pos -= 1

        count += (temp_left_pos - left_pos) * (right_pos - temp_right_pos)
        left_pos, right_pos = temp_left_pos, temp_right_pos
    elif ab[left_pos] + cd[right_pos] > 0:
        right_pos -= 1
    else:
        left_pos += 1

print(count)