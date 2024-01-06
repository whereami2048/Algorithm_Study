import sys
input = sys.stdin.readline

n = int(input())  
nums = list(map(int, input().split()))
dp = [1 for _ in range(n)]

# 길이 구하는 for문
for i in range(n):
  for j in range(i):
    if nums[i] > nums[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 수열 출력을 위한 for문
max_dp = max(dp)
arr = []
for i in range(n-1, -1, -1):
  if dp[i] == max_dp:
    arr.append(nums[i])
    max_dp -= 1

arr.reverse()
for i in arr:
    print(i, end=" ")