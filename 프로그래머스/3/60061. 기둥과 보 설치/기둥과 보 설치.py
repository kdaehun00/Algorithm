"""
기둥(0) - 기둥 위, 보 위, 바닥 위
보(1) - 양쪽이 보, 한쪽이 기둥 위

입력 - x, y + a + b
x, y = 좌표
a = 기둥(0), 보(1)
b = 삭제(0), 설치(1)
"""

def possible(answer):
    for x, y, a in answer:
        if a == 0:
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                [x - 1, y, 1] in answer and [x + 1, y, 1] in answer
            ):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
    return sorted(answer)