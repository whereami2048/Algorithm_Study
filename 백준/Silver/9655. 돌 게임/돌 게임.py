n = int(input())

dp = ["" for _ in range(n + 1)]

# dp[1] = "SK"
# dp[2] = "CY"
# dp[3] = "SK"
# dp[4] = "CY"
#
# for i in range(4, n + 1):
#     if dp[i - 1] == "SK":
#         dp[i] = "CY"
#     else:
#         dp[i] = "SK"

if n % 2 == 1:
    print("SK")
else:
    print("CY")