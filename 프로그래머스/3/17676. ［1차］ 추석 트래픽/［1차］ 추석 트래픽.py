def solution(lines):
    def to_mills(time):
        hour, minute, second = time.split(":")
        return (int(hour) * 3600 + int(minute) * 60 + float(second)) * 1000
    
    line_list = []
    for line in lines:
        date, time, duration = line.split()
        duration = float(duration[:-1]) * 1000
        end_time = to_mills(time)
        start_time = end_time - duration + 1
        line_list.append((start_time, end_time))
        
    answer= 0
    
    for s, e in line_list:
        start_target = e
        end_target = e + 999
        
        count = 0
        for s2, e2 in line_list:
            if s2 <= end_target and e2 >= start_target:
                count += 1
            answer = max(answer, count)
            
    return answer