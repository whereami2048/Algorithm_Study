def solution(edges):
    answer = [-1, 0, 0, 0]
    edges_dict = {}
    
    for start, end in edges:
        if edges_dict.get(start):
            edges_dict[start][1] += 1
        else:
            edges_dict[start] = [0, 1]
        
        if edges_dict.get(end):
            edges_dict[end][0] += 1
        else:
            edges_dict[end] = [1, 0]
    
    for key, val in edges_dict.items():
        if val[0] == 0 and val[1] >= 2: # 생성된 정점
            answer[0] = key
        
        if val[0] > 0 and val[1] == 0: # 막대
            answer[2] += 1
        
        if val[0] >= 2 and val[1] >= 2: # 팔자
            answer[3] += 1
    
    answer[1] = edges_dict[answer[0]][1] - (answer[2] + answer[3])
    
    return answer