def solution(priorities, location):
    answer = 0
    
    priorities = [(index, value) for index, value in enumerate(priorities)]
    
    while priorities:
        first = priorities.pop(0)
        if any(first[1] < temp[1] for temp in priorities):
            priorities.append(first)
        else:
            answer += 1
            if first[0] == location:
                return answer
    
    return answer