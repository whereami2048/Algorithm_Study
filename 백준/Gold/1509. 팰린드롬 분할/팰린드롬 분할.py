import sys

sys.setrecursionlimit(10000000)

arr = list(input())
size = len(arr)

is_palindrome = [[False for _ in range(size)] for _ in range(size)]
dp = [2500 for _ in range(size + 1)]
dp[-1] = 0

for i in range(size):
    is_palindrome[i][i] = True

for i in range(1, size):
    if arr[i-1] == arr[i]:
        is_palindrome[i-1][i] = True

for i in range(3, size + 1):
    for start in range(size - i + 1):
        end = start + i - 1
        if arr[start] == arr[end] and is_palindrome[start + 1][end - 1]:
            is_palindrome[start][end] = True

for end in range(size):
    for start in range(end + 1):
        if is_palindrome[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)
        else:
            dp[end] = min(dp[end], dp[end - 1] + 1)

print(dp[size - 1])
