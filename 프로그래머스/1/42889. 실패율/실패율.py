from collections import Counter
def solution(N, stages):
    answer = []
    stage_fail_rate = []
    stage_num = len(stages)
    data_set = Counter(stages)
    for i in range(1, N+1):
        data_len = data_set.get(i, 0)
        if stage_num > 0:
            fail_rate = data_len / stage_num
        else:
            fail_rate = 0
        stage_fail_rate.append((i, fail_rate))
        stage_num -= data_len
        
    stage_fail_rate.sort(key=lambda x: (-x[1], x[0]))
    
    answer = [stage for stage, rate in stage_fail_rate]
        
    return answer