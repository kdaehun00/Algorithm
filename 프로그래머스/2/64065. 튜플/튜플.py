from collections import defaultdict
def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    db = defaultdict(int)
    for tup in s:
        tup = tup.split(",")
        for num in tup:
            db[num] += 1

    for key, value in sorted(db.items(), key=lambda x: x[1], reverse=True):
        answer.append(int(key))
        
    return answer