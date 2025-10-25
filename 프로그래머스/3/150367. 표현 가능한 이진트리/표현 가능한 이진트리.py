def can_make_tree(binary_code):
    mid = len(binary_code) // 2
    root = binary_code[mid]
    
    if len(binary_code) == 1:
        return True
    
    left = binary_code[:mid]
    right = binary_code[mid+1:]
    
    if root == '0' and ('1' in left or '1' in right):
        return False
    
    return can_make_tree(left) and can_make_tree(right)

    
def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = bin(num)[2:]
        
        h = 1
        while (2**h-1) < len(bin_num):
            h += 1
        
        binary_code = bin_num.zfill(2**h-1)
        answer.append(1 if can_make_tree(binary_code) else 0)
    return answer