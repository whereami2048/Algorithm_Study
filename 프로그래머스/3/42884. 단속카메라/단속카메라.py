def solution(routes):
    answer = 1
    routes.sort(key =lambda x : x[1], reverse = True)
    pos = routes.pop()[1]
    
    while len(routes) != 0:
        target = routes.pop()
        
        if target[0] > pos:
            print(target[0])
            pos = target[1]
            answer += 1
    
    return answer