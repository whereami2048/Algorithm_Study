def solution(cards):
    answer = 0
    visited = [False for _ in range(len(cards))]
    combinations = []
    
    def open(index, combination, visited):
        if visited[index]:
            return combination
        
        visited[index] = True
        combination.append(index)
        return open(cards[index] - 1, combination, visited)
    
    for i in range(len(cards)):
        combinations.append(len(open(i, [], visited)))
        
        if False not in visited:
            break
    
    combinations.sort(reverse = True)
    
    if len(combinations) == 1:
        return 0
    
    return combinations[0] * combinations[1]