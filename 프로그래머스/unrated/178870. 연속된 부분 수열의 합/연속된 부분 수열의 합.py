def solution(sequence, k):
    answer = []
    sub_amount = 0
    start = end = 0
    min_len = len(sequence)
    for start in range(len(sequence)):
        while(sub_amount < k and end < len(sequence)):
            sub_amount += sequence[end]
            end += 1
        
        if sub_amount == k and end-1-start < min_len:
            min_len = end - 1 - start
            answer = [start, end-1]
        
        sub_amount -= sequence[start]
    
    
    return answer