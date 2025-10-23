def solution(n, s, a, b, fares):
    INF = int(1e9) 
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0
        
    for v1, v2, fee in fares:
        graph[v1][v2] = fee
        graph[v2][v1] = fee
    
    for k in range(1, n+1):
        for y in range(1, n+1):
            for x in range(1, n+1):
                if graph[y][x] > graph[y][k] + graph[k][x]:
                    graph[y][x] = graph[y][k] + graph[k][x]
                
    answer = INF
    for i in range(1, n+1):
        total = graph[s][i] + graph[i][a] + graph[i][b]
        answer = min(answer, total)
        
    return answer