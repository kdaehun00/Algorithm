from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache_data = deque(maxlen=cacheSize)
    if not cacheSize:
        return 5*len(cities)
    
    for city in cities:
        city = city.lower()
        if city in cache_data:
            cache_data.remove(city)
            cache_data.appendleft(city)
            answer += 1
        else:
            cache_data.appendleft(city)
            answer += 5
    return answer