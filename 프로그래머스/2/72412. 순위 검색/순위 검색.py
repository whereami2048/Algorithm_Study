from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

def solution(infos, queries):
    answer = []
    
    key_dict = defaultdict(list)
    
    for info in infos:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])
        
        for i in range(5):
            combi = list(combinations([0,1,2,3], i))
            for c in combi:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                key_dict[key].append(score)
    
    for value in key_dict.values():
        value.sort()
        
    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        
        if target_key in key_dict:
            target_list = key_dict[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
    
    return answer