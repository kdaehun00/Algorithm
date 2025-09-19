"""
n = 한 변의 길이
벽 = #, 공백 = ""

1. 숫자를 이진수로 변환
2. 1 을 #로, 0을 공백으로 변경
3. arr1 과 arr2 를 겹쳐서 최종 배열 완성
"""
def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        row = bin(a | b)[2:]
        row = row.zfill(n)
        
        row = row.replace('1', '#').replace('0', ' ')
        answer.append(row)
    
    return answer