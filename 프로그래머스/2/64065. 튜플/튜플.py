def solution(s):
    set_list = []
    answer = []
    inner_set = s[2:-2].split('},{')
    
    for target in inner_set:
        set_list.append(list(map(int, target.split(','))))
    
    set_list.sort(key=len)
    num_set = set()
    for target in set_list:
        answer.append(list(set(target) - num_set)[0])
        num_set = num_set | set(target)
        
    return answer