from math import trunc

def solution(enroll, referral, seller, amount):
    
    def distribute_profit(salesman, cost):
        dist_cost = trunc(cost * 0.1)
        answer[salesman] += cost - dist_cost
        
        if dist_cost >= 1:
            refer = refer_map[salesman]

            if refer != '-':
                distribute_profit(refer, dist_cost)
        else:
            answer[salesman] += dist_cost
            
    answer = {name: 0 for name in enroll}
    refer_map = {enroll[i]: referral[i] for i in range(len(enroll))}

    for i in range(len(amount)):
        profit = amount[i] * 100
        dist_cost = trunc(profit * 0.1)
        answer[seller[i]] += profit - dist_cost

        refer = refer_map[seller[i]]        
        if refer != '-':
            distribute_profit(refer, dist_cost)
    
    result = []
    for i in range(len(enroll)):
        result.append(answer[enroll[i]])
        
    return result