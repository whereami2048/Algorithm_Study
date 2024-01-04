n = int(input())

children = []

for _ in range(n):
    children.append(int(input()))

dp = [0 for _ in range(n)]
dp[0] = 1
temp = 0

for i in range(1,n):
      for j in range(0,i):
         if children[i] > children[j]:
            temp = max(temp,dp[j])
      dp[i]=temp+1
      temp=0

print(n-max(dp))