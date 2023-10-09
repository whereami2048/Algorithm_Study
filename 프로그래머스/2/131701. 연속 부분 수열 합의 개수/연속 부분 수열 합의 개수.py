def solution(elements):
    answer = 0
    result_set = set()
    n = len(elements)    
    for i in range(1, n+1):
        circle_elements = elements + elements[:i]        
        for j in range(n):
            result_set.add(sum(circle_elements[j : j+i]))
        
    return len(result_set)