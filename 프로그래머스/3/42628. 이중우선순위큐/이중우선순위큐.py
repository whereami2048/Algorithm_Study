import heapq

def solution(operations):
    answer = []
    arr = []
    
    for operation in operations:
        op_code, target = operation.split()
        if op_code == 'I':
            arr.append(int(target))
            arr.sort()
        else:
            if target == '1':
                if arr:
                    del arr[-1]
            else:
                if arr:
                    del arr[0]
                    
    if arr:
        return [arr[-1], arr[0]]
    else:
        return [0, 0]