N, L = map(int, input().split())

for k in range(L, 101):
    temp = N - k * (k - 1) // 2
    if temp < 0:
        continue
    if temp % k == 0:
        x = temp // k
        if x >= 0:
            print(*range(x, x + k))
            break
else:
    print(-1)