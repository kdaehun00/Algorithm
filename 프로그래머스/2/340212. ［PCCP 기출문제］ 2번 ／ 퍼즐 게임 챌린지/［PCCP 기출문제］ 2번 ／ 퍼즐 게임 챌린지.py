def solution(diffs, times, limit):
    n = len(diffs)
    
    def can_clear(level):
        total = times[0]
        
        for i in range(1, n):
            if diffs[i] <= level:
                total += times[i]
            else:
                miss = diffs[i] - level
                total += miss * (times[i] + times[i-1]) + times[i]
            
            if total > limit:
                return False
        
        return total <= limit
    
    left, right = 1, max(diffs)
    
    while left < right:
        mid = (left + right) // 2
        if can_clear(mid):
            right = mid
        else:
            left = mid + 1
    
    return left