from collections import Counter

def solution(str1, str2):
    def split_str(data):
        data = data.lower()
        data_list = []
        for i in range(len(data) - 1):
            a, b = data[i], data[i + 1]
            if a.isalpha() and b.isalpha():
                data_list.append(a + b)
        return data_list
    
    str1_list = split_str(str1)
    str2_list = split_str(str2)
    
    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)
    
    intersection = counter1 & counter2
    union = counter1 | counter2
    
    inter_size = sum(intersection.values())
    union_size = sum(union.values())
    
    if union_size == 0:
        return 65536
    return int(inter_size / union_size * 65536)