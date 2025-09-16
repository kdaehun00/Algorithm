def solution(survey, choices):
    scores = {ch: 0 for ch in "RTCFJMAN"}
    
    for s, c in zip(survey, choices):
        disagree, agree = s[0], s[1]
        if c < 4:
            scores[disagree] += 4 - c
        elif c > 4:
            scores[agree] += c - 4
    
    result = ""
    pairs = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    
    for a, b in pairs:
        if scores[a] > scores[b]:
            result += a
        elif scores[a] < scores[b]:
            result += b
        else:
            result += min(a, b)

    return result