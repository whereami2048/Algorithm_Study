from sys import stdin

n = int(input())
target = list(map(int, stdin.readline().split()))

max_dp = target
min_dp = target

for _ in range(n - 1):
    target = list(map(int, stdin.readline().split()))

    max_dp = [target[0] + max(max_dp[0], max_dp[1]), target[1] + max(max_dp), target[2] + max(max_dp[1], max_dp[2])]
    min_dp = [target[0] + min(min_dp[0], min_dp[1]), target[1] + min(min_dp), target[2] + min(min_dp[1], min_dp[2])]

print(max(max_dp), min(min_dp))