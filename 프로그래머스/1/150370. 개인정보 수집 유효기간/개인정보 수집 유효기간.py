from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    db = defaultdict(int)
    for term in terms:
        category, period = term.split()
        db[category] = int(period)
    
    def convert_date(date):
        y, m, d = date.split(".")
        return 28*(12*int(y) + int(m)) + int(d)
    
    today = convert_date(today)
    
    def convert_end_date(date, period):
        return convert_date(date) + period*28
        
    for i, privacy in enumerate(privacies):
        date, category = privacy.split()
        end_date = convert_end_date(date, db[category])
        
        if end_date <= today:
            answer.append(i+1)
        
    return answer