def solution(stones, k):
    left, right = 1, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        can_cross = True
        
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
                if cnt >= k:
                    can_cross = False
                    break
            else:
                cnt = 0
                
        if can_cross:
            left = mid + 1
        else:
            right = mid - 1
            
    return right