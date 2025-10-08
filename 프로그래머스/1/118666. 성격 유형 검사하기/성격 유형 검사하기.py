from collections import defaultdict

def solution(survey, choices):
    answer = ''
    mbti_list = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    set_score = 4
    db = defaultdict(int)
    
    for data, score in zip(survey, choices):
        a = data[0]
        b = data[1]
        
        if score <= 4:
            db[a] += set_score - score
        else:
            db[b] += score - set_score
    
    for a, b in mbti_list:
        if db[a] > db[b]:
            answer += a
        elif db[a] < db[b]:
            answer += b
        else:
            if ord(a) < ord(b):
                answer += a
            else:
                answer += b
    return answer