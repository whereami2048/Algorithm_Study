def solution(n, computers):
    answer = 0
    
    visited = [False for _ in range(n)]

    def dfs(pos):        
        visited[pos] = True

        for i in range(n):
            if computers[pos][i] == 1 and not visited[i]:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
            
    return answer