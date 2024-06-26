def solution(n, stations, w):
    answer = 0
    std = w * 2 + 1
    pos = 1
    
    for station in stations:
        if station - w - pos > 0:
            answer += (station - w - pos) // std
            
            if (station - w - pos) % std:
                answer += 1
                
        pos = station + w + 1
        
    if n - pos + 1 > 0:
        answer += (n - pos + 1) // std
        
        if (n - pos + 1) % std:
            answer += 1
            
    return answer