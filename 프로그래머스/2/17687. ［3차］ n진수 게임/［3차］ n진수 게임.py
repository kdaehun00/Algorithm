def solution(n, t, m, p):
    digits = "0123456789ABCDEF"
    
    def convert(num, base):
        if num == 0:
            return "0"
        res = ""
        while num > 0:
            num, r = divmod(num, base)
            res = digits[r] + res
        return res
    
    full_str = ""
    num = 0
    while len(full_str) < t * m:
        full_str += convert(num, n)
        num += 1

    answer = ''.join(full_str[p - 1 + i * m] for i in range(t))
    return answer