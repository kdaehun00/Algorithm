import math
def solution(n, k):
    count = 0
    def convert_k_code(num, k):
        if num == 0:
            return "0"
        code = ""
        while num > 0:
            num, data = divmod(num, k)
            code = str(data) + code
        return code
    
    def chk_prime(num):
        num = int(num)
        if num < 2:
            return False
        
        for i in range(2, int(math.sqrt(num))+1):
            if not num % i:
                return False
            
        return True
    
    code = convert_k_code(n, k)
    prime_list = code.split("0")
    
    for num in prime_list:
        if not num:
            continue
            
        if chk_prime(num):
            count += 1
        
    return count