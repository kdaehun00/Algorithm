"""
아이디: 3자 이상 15자 이하 (알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 사용가능)
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

소문자 치환
문자 제거
연속 .를 하나로 치환
.이 처음이나 끝에 있으면 제거
빈 문자열이면 a 대입
16글자면 뒤에 제거, 끝에 마침표 있으면 제거
마지막 글자 반복으로 3글자 이상 만들기
"""
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    disable_list = [
        '~', '!', '@', '#', '$', '%', '^', '&', '*', 
        '(', ')', '=', '+', '[', '{', ']', '}', 
        ':', '?', ',', '<', '>', '/'
    ]    

    for disable_word in disable_list:
        new_id = new_id.replace(disable_word, '')
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    new_id = new_id.strip('.')
    
    if not new_id:
        new_id = "a"
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
    
    new_id = new_id.strip('.')
    
    while len(new_id) < 3:
        new_id += new_id[-1]
        
    return new_id