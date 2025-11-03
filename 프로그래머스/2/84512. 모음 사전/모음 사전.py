def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    weight = [781, 156, 31, 6, 1]

    answer = 0
    for i, ch in enumerate(word):
        answer += alpha.index(ch) * weight[i] + 1

    return answer