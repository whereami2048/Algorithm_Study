def solution(arrayA, arrayB):
    answer = 0
    
    def gcd(a, b):
        while b > 0:
            temp = a % b
            a = b
            b = temp
        
        return a
    
    max_gcd_a, max_gcd_b = arrayA[0], arrayB[0]
        
    for arr_a in arrayA[1:]:
        max_gcd_a = gcd(max_gcd_a, arr_a)
        
    for arr_b in arrayB[1:]:
        max_gcd_b = gcd(max_gcd_b, arr_b)
    
    listA, listB = [], []
    
    for i in range(max_gcd_a, 0, -1):
        if max_gcd_a % i == 0:
            listA.append(i)
            
    for i in range(max_gcd_b, 0, -1):
        if max_gcd_b % i == 0:
            listB.append(i)
            
    resultA, resultB = 0, 0
    for num in listA:
        flag = True
        for arr_b in arrayB:
            if arr_b % num == 0:
                flag = False
                break
        
        if flag:
            resultA = max(num, resultA)
            
    for num in listB:
        flag = True
        for arr_a in arrayA:
            if arr_a % num == 0:
                flag = False
                break
        
        if flag:
            resultB = max(num, resultB)
            
    return max(resultA, resultB)