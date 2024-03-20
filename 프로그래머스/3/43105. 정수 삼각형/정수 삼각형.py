def solution(triangle):
    answer = 0
    dp = [[0 for _ in range(i+1)] for i in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
    
    n = len(dp)
    
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]
    
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]
    
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
    
    return max(dp[n-1])