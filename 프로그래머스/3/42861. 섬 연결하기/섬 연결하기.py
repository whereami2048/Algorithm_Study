def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) 
    family = set([costs[0][0]])

    while len(family) != n:
        for cost in costs:
            if cost[0] in family and cost[1] in family:
                continue
            if cost[0] in family or cost[1] in family:
                family.update([cost[0], cost[1]])
                answer += cost[2]
                break
                
    return answer
    
    
        