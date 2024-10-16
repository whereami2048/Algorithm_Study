def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n)] for _ in range(n)]
    
    for a, b in results:
        graph[a-1][b-1] = 1
        
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[j][k] == 0 and graph[j][i] and graph[i][k]:
                    graph[j][k] = 1
                    
    row_cnt = [0 for _ in range(n)]
    col_cnt = [0 for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            col_cnt[col] += graph[row][col]
            row_cnt[row] += graph[row][col]
    
    for i in range(n):
        if row_cnt[i] + col_cnt[i] == n-1: 
            answer += 1
    return answer
                
    return answer