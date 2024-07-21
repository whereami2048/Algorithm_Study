import bisect

t = int(input())

n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

n_sum_arr = []
m_sum_arr = []

for i in range(n):
    for j in range(i + 1, n + 1):
        n_sum_arr.append(sum(n_arr[i:j]))

for i in range(m):
    for j in range(i + 1, m + 1):
        m_sum_arr.append(sum(m_arr[i:j]))

n_sum_arr.sort()
m_sum_arr.sort()

result = 0

for n_num in n_sum_arr:
    diff = t - n_num
    left_pos = bisect.bisect_left(m_sum_arr, diff)
    right_pos = bisect.bisect_right(m_sum_arr, diff)

    result += right_pos - left_pos

print(result)
