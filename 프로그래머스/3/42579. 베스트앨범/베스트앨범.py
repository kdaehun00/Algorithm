from collections import defaultdict

def solution(genres, plays):
    music_time = defaultdict(int)
    music_db = defaultdict(list)
    
    for i in range(len(genres)):
        music_time[genres[i]] += plays[i]
        music_db[genres[i]].append([i, plays[i]])
    
    sorted_genres = sorted(music_time.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for genre, _ in sorted_genres:
        sorted_songs = sorted(music_db[genre], key=lambda x: (-x[1], x[0]))
        result.extend([idx for idx, _ in sorted_songs[:2]])
    
    return result