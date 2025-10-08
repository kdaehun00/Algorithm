"""
소문자 치환
-, _, . 빼고 모두 제거
.. -> . 로 치환
앞뒤 . 제거
빈 문자열이면 a 대입
16글자 이상이면 15글자로 정리 후 앞뒤 .제거
2글자 이하면 끝문자 반복 3이상일 때까지
"""
def solution(new_id):
    answer = ''
    can_not = "~!@#$%^&*()=+[{]}:?,<>/"
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for word in can_not:
        new_id = new_id.replace(word, "")
    
    # 3단계
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    
    # 4단계
    new_id = new_id.strip(".")
    
    # 5단계
    if len(new_id) <= 0:
        new_id += 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip(".")
        
    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
    return new_id