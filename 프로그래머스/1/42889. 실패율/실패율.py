def solution(N, stages):

    users = len(stages)
    fail_rate_list = [0 for _ in range(N+1)]
    
    for i in range(1, N+1):
        if i in stages:
            fail = stages.count(i)
            fail_rate_list[i] = fail / users
            users -= fail
            stages.remove(i)
    
    answer = [i for i, v in sorted(enumerate(fail_rate_list[1:], start=1), key=lambda x: -x[1])]

    return answer