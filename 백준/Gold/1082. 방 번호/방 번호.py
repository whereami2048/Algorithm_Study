import sys

n= int(input())

price = (list(map(int, input().split())))
number = [i for i in range(n)]
money = int(input())
dp=[-sys.maxsize]* (money+1)
result=[]

for i in range(n-1, -1, -1):
  number_price =  price[i]
  
  for j in range(number_price, money+1):
    dp[j]= max(dp[j], dp[j-number_price]*10+number[i], number[i])

print(dp[money])