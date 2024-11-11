from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
        
    unique_list = []
    for comb in combi:
        tmp = [tuple([item[key] for key in comb]) for item in relation]

        if len(set(tmp)) == row: 
            flag = True
            
            for unique in unique_list:
                if set(unique).issubset(set(comb)):
                    flag = False
                    break
                    
            if flag: 
                unique_list.append(comb)
   
    return len(unique_list)