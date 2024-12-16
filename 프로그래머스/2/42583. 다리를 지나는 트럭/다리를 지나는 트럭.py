from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    answer = 1
    move_trucks = [[truck_weights.popleft(), 1]]
    sum_truck_weight = move_trucks[0][0]
    
    while truck_weights or move_trucks:
        if truck_weights and len(move_trucks) < bridge_length and sum_truck_weight + truck_weights[0] <= weight:
            move_trucks.append([truck_weights.popleft(), 0])

            sum_truck_weight += move_trucks[-1][0]
            
        for truck in move_trucks:
            truck[1] += 1
        
        for truck in move_trucks:
            if truck[1] >= bridge_length:
                sum_truck_weight -= truck[0]
                move_trucks.remove(truck)

        answer += 1
        
    return answer + 1