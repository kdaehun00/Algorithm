def solution(N, stages):

    users = len(stages)
    fail_rate_list = []
    
    for i in range(1, N+1):
        if i in stages:
            fail = stages.count(i)
            fail_rate_list.append((i, fail / users))
            users -= fail
            stages.remove(i)
        else:
            fail_rate_list.append((i, 0))

    
    fail_rate_list.sort(key= lambda x: (-x[1], x[0]))
    
    answer = [stage for stage, rate in fail_rate_list]
    return answer