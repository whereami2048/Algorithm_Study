def solution(progresses, speeds):
    days = []
    answer = []
    for i in range(len(progresses)):
        rest_progress = 100 - progresses[i]
        rest_days = rest_progress // speeds[i]
        
        if rest_progress % speeds[i]:
            rest_days += 1
            
        days.append(rest_days)
        
    while days:
        target_day = days.pop(0)
        count = 1
        for i in range(len(days)):
            if days[i] > target_day:
                break
            count += 1
        
        for _ in range(count - 1):
            days.pop(0)
            
        answer.append(count)
        
    return answer
