def solution(cap, n, deliveries, pickups):
    answer = -1
    
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    cur_delivery = 0
    cur_pickups = 0
    
    for i in range(n):
        cur_delivery += deliveries[i]
        cur_pickups += pickups[i]
        
        while cur_delivery > 0 or cur_pickups > 0:
            cur_delivery -= cap
            cur_pickups -= cap
            answer += (n - i) * 2
    
    return answer + 1