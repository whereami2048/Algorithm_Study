def solution(n, money):
    dp = [1] + [0] * n
    
    for m in money:
        for cur in range(m, n + 1):
            dp[cur] += dp[cur - m]
    
    return dp[n] % 1000000007