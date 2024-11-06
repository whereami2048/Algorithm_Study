def solution(begin, end):
    answer = []
    
    def max_division(target):
        temp = [1]
        if target == 1:
            return 0
        for i in range(2, int(target**(1/2)) + 1):
            if target % i == 0 and i < 10**7:
                temp.append(i)
                if target//i <=10**7 and target//i != target:
                    temp.append(target//i)
        
        return max(temp)
    
    for pos in range(begin, end + 1):
        answer.append(max_division(pos))
            
    return answer