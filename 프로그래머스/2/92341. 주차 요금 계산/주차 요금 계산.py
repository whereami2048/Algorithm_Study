import math

def compute_parking_time(in_time, out_time):
    in_hour, in_minute = map(float, in_time.split(':'))
    out_hour, out_minute = map(float, out_time.split(':'))
    
    return (out_hour - in_hour) * 60 + out_minute - in_minute

def solution(fees, records):
    answer = []
    records = [record.split() for record in records]
    
    current_parking = {}
    parking_time = {record[1]: 0 for record in records}
    
    for time, car_num, status in records:
        if status == 'IN': # 입차인 경우
            current_parking[car_num] = time
        else: # 출차인 경우
            in_time = current_parking[car_num]
            parking_time[car_num] += compute_parking_time(in_time, time)
            del(current_parking[car_num])
    
    for car_num, in_time in current_parking.items():
        parking_time[car_num] += compute_parking_time(in_time, '23:59')
        
    for car_num, total_time in parking_time.items():
        if total_time <= fees[0]: # 누적 시간이 기본 시간 이하인 경우
            answer.append((car_num, fees[1]))
        else: # 누적 시간이 기본 시간 초과인 경우
            over_time = total_time - fees[0]
            over_fee = math.ceil((over_time / fees[2])) * fees[3]
            answer.append((car_num, over_fee + fees[1]))
    
    return list(map(lambda x: x[1], sorted(answer, key=lambda x: x[0])))
