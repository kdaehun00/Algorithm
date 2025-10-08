def solution(numbers, hand):
    result = ''
    pad = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2),
        "*": (3, 0), "0": (3, 1), "#": (3, 2)
    }
    
    n_left = pad["*"]
    n_right = pad["#"]
        
    for num in numbers:
        if num in [1, 4, 7]:
            n_left = pad[str(num)]
            result += "L"
        elif num in [3, 6, 9]:
            n_right = pad[str(num)]
            result += "R"
        else:
            target_y, target_x = list(pad[str(num)])
            left_dist = abs(n_left[0] - target_y) + abs(n_left[1] - target_x)
            right_dist = abs(n_right[0] - target_y) + abs(n_right[1] - target_x)
            
            if left_dist > right_dist:
                n_right = pad[str(num)]
                result += "R"
                
            elif left_dist < right_dist:
                n_left = pad[str(num)]
                result += "L"
                
            else:
                if hand == "right":
                    n_right = pad[str(num)]
                    result += "R"
                    
                if hand == "left":
                    n_left = pad[str(num)]
                    result += "L"       
    
    return result