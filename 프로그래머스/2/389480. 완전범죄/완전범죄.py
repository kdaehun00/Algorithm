def solution(info, n, m):
    INF = 10**9
    dp = [INF] * m
    dp[0] = 0

    for a_i, b_i in info:
        newdp = [INF] * m
        for b in range(m):
            if dp[b] == INF:
                continue

            a_sum = dp[b] + a_i
            if a_sum < n:
                if a_sum < newdp[b]:
                    newdp[b] = a_sum

            b2 = b + b_i
            if b2 < m:
                if dp[b] < newdp[b2]:
                    newdp[b2] = dp[b]

        dp = newdp

    ans = min(dp)
    return ans if ans != INF else -1