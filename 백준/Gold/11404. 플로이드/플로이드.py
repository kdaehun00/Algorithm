import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

db = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
  db[i][i] = 0

for i in range(m):
  a, b, fee = map(int, input().split())
  db[a][b] = min(db[a][b], fee)

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      db[a][b] = min(db[a][b], db[a][k] + db[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if db[i][j] == INF:
            print(0, end=" ")  # 경로 없음
        else:
            print(db[i][j], end=" ")
    print()