import heapq

def solution(jobs):
    answer, now, cnt = 0, 0, 0
    recent_done = -1
    queue = []
    
    while cnt < len(jobs):
        for job in jobs:
            if recent_done < job[0] <= now:
                heapq.heappush(queue, [job[1], job[0]])
    
        if queue:
            new_job = heapq.heappop(queue)
            recent_done = now
            cnt += 1
            now += new_job[0]
            answer += now - new_job[1]
        else:
            now += 1
    
    return answer // len(jobs)