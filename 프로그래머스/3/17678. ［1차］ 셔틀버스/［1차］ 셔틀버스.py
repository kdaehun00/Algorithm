"""
n회 t분 간격, m명 탑승
"""
from collections import deque
def solution(n, t, m, timetable):
    
    def txt_time_convert(txt):
        hour, minute = txt.split(":")
        return int(hour)*60 + int(minute)
    
    def time_txt_convert(time):
        hour, minute = divmod(time, 60)
        return f"{hour:02d}:{minute:02d}"
    
    start_time = txt_time_convert("09:00")
    timetable = sorted([txt_time_convert(x) for x in timetable])
    timetable = deque(timetable)
    bus_times = [start_time + i * t for i in range(n)]
    for bus_time in bus_times:
        onboard = []
        while timetable and timetable[0] <= bus_time and len(onboard) < m:
            onboard.append(timetable.popleft())
        
        if bus_time == bus_times[-1]:
            if len(onboard) < m:
                return time_txt_convert(bus_time)
            else:
                return time_txt_convert(onboard[-1] -1)
        