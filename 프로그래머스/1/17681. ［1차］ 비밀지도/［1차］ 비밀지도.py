from collections import deque

def solution(n, arr1, arr2):
    answer = []
    
    def convert_binary(num):
        binary_code = deque()
        while num > 0:
            num, data = divmod(num, 2)
            binary_code.appendleft(data)
        while len(binary_code) < n:
            binary_code.appendleft(0)
        return binary_code
    
    for i in range(n):
        b1 = convert_binary(arr1[i])
        b2 = convert_binary(arr2[i])
        data = ""
        for bit1, bit2 in zip(b1, b2):
            if bit1 or bit2:
                data += "#"
            else:
                data += " "
        answer.append(data)
        
    return answer