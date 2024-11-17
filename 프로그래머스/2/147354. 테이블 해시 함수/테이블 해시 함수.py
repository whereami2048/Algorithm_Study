from functools import reduce

def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    
    total_si = []
    for i in range(row_begin, row_end + 1):
        total_si.append(sum(map(lambda x: x % i, data[i - 1])))
        
    answer = reduce(lambda x, y: x ^ y, total_si)
    return answer