from itertools import product
def solution(users, emoticons):
    answer = []
    discount_rate = [10, 20, 30, 40]
    
    for discount_rate in product(discount_rate, repeat=len(emoticons)):
        join, disc = 0, 0
        
        for d, limit in users:
            total = 0
            for emoticon, discount in zip(emoticons, discount_rate):
                if discount >= d:
                    total += emoticon * ((100-discount) / 100)
            
            if total >= limit:
                join += 1
            else:
                disc += total
                
        answer.append((join, disc))
    
    answer.sort(key=lambda x: (-x[0], -x[1]))
    return answer[0]