"""
N - 추의 개수 ( 1 <= N <= 1000 )
weight_list - 추의 무게들 ( 1 <= S < 1,000,000 )
"""
import sys

input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
weights.sort()

target = 1

for w in weights:
    if w > target:
        break
    target += w

print(target)