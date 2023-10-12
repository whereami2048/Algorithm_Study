def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):
        products = discount[i: i+10]
        flag = True
        for w in range(len(want)):
            if want[w] not in products:
                flag = False
                break
            elif number[w] > products.count(want[w]):
                flag = False
                break
            
        if flag:
            answer += 1
        
    return answer