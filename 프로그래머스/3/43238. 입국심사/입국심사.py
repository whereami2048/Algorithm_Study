def solution(n, times):
    left_time = min(times)
    right_time = max(times) * n
    
    while left_time <= right_time:
        mid_time = (left_time + right_time) // 2
        customers = 0
        
        for time in times:
            customers += mid_time // time
            
            if customers >= n:
                break
        
        if customers >= n:
            right_time = mid_time - 1
        else:
            left_time = mid_time + 1
    
    return left_time