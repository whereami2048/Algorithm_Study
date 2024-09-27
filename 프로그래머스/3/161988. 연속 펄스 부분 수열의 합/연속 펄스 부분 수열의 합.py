def solution(sequence):
    size = len(sequence)
    temp = lambda x: 1 if x % 2 else -1
    sequence = [temp(i) * sequence[i] for i in range(size)]
    
    dp = [[0, 0] for _ in range(size)]
    dp[0] = [sequence[0], sequence[0]]
    
    for i in range(1, size):
        cur = sequence[i]
        
        dp[i][0] = min(cur, dp[i-1][0] + cur)
        dp[i][1] = max(cur, dp[i-1][1] + cur)
        
    min_val = min(map(min, dp))
    max_val = max(map(max, dp))

    return max(abs(min_val), abs(max_val))