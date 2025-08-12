from collections import defaultdict
from itertools import combinations
import bisect

def solution(info, query):
    db = defaultdict(list)
    for i in info:
        parts = i.split()
        conditions = parts[:-1]
        cost = int(parts[-1])
        for r in range(5):
            for comb in combinations(range(4), r):
                temp = conditions[:]
                for idx in comb:
                    temp[idx] = '-'
                key = ' '.join(temp)
                db[key].append(cost)

    for key in db:
        db[key].sort()

    answer = []
    for q in query:
        q = q.replace(' and ', ' ')
        parts = q.split()
        key = ' '.join(parts[:-1])
        cost = int(parts[-1])

        if key in db:
            costs = db[key]
            idx = bisect.bisect_left(costs, cost)
            answer.append(len(costs) - idx)
        else:
            answer.append(0)

    return answer