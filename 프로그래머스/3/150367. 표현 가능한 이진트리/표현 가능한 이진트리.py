def solution(numbers):
    answer = []
    bins = [2**i - 1 for i in range(50)]
    
    def dfs(target):
        size = len(target)
        
        if size == 1:
            return True
        
        if '0' not in target or '1' not in target:
            return True
        
        mid = size // 2
        if target[mid] == '0':
            return False
        
        return dfs(target[:mid]) and dfs(target[mid + 1:])
    
    
    for num in numbers:
        binary_num = bin(num)[2:]
        
        for bin_num in bins:
            if bin_num >= len(binary_num):
                binary_num = '0'*(bin_num - len(binary_num)) + binary_num
                break

        answer.append(1 if dfs(binary_num) else 0)
        
    return answer