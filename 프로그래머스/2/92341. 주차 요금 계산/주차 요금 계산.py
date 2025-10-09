"""
기본시간, 기본요금, 추가시간, 추가요금
"""
from collections import defaultdict
import math
def solution(fees, records):
    default_time, default_fee, add_time, add_fee = fees
    def convert_time(txt):
        hour, minute = txt.split(":")
        return int(hour)*60 + int(minute)
    last_time = convert_time("23:59")

    answer = []
    park_db = defaultdict(int)
    time_db = defaultdict(int)
    
    for record in records:
        time_txt, car_num, status = record.split()
        time = convert_time(time_txt)
        if status == "IN":
            park_db[car_num] = time
        elif status == "OUT":
            time_db[car_num] += time - park_db[car_num]
            park_db[car_num] = -1
    
    for car_num, time in park_db.items():
        if time >= 0:
            time_db[car_num] += last_time - time
                
    for car_num, time in sorted(time_db.items()):
        fee = 0
        if time >= 0:
            time -= default_time
            fee += default_fee
            if time > 0:
                fee += (math.ceil(time / add_time) * add_fee)
        answer.append(fee)
        
    return answer