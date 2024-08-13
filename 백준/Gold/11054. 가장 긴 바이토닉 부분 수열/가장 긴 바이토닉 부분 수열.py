n = int(input())
arr = list(map(int, input().split()))

desc_arr = arr[::-1]

inc_dp = [1 for _ in range(n)]
desc_dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)

        if desc_arr[i] > desc_arr[j]:
            desc_dp[i] = max(desc_dp[i], desc_dp[j] + 1)

desc_dp = desc_dp[::-1]

result = []

for i in range(n):
    result.append(inc_dp[i] + desc_dp[i] - 1)

print(max(result))
