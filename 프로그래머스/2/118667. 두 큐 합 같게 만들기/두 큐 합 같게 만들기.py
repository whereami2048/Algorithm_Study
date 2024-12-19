from collections import deque

def solution(queue1, queue2):
    answer = -1
    sum1, sum2 = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    origin_count = len(queue1)
    count = 0
    move_count = 0
    
    while count != origin_count * 2:
        if sum1 == sum2:
            answer = move_count
            break
            
        if sum1 > sum2:
            move_var = queue1.popleft()
            sum1 -= move_var
            queue2.append(move_var)
            sum2 += move_var
            count += 1
        else:
            move_var = queue2.popleft()
            sum2 -= move_var
            queue1.append(move_var)
            sum1 += move_var
        
        move_count += 1
        
    return answer