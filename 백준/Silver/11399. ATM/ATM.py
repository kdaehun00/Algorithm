n = int(input())
p = list(map(int, input().split()))

p.sort()

total = 0
answer = 0

for time in p:
    total += time
    answer += total

print(answer)