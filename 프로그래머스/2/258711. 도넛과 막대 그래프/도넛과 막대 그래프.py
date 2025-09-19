"""
정점마다 계산하기.

정점 제외 기준

1. 도넛 모양
- in이랑 out이 같다.
- 간선수 = 정점수

2. 막대 모양
- in, out = 0

3. 8자 모양
in = out = 2

"""
from collections import defaultdict
def solution(edges):
    answer = []
    in_db = defaultdict(int)
    out_db = defaultdict(int)
    max_node = 0
    node = 0
    
    donut_graph = 0
    list_graph = 0
    eight_graph = 0
    
    for a, b in edges:
        out_db[a] += 1
        in_db[b] += 1
        
        max_num = max(a, b)
        if max_num > max_node:
            max_node = max_num
    
    for i in range(1, max_node+1):
        if out_db[i] >= 2 and in_db[i] == 0:
            node = i
            
        elif out_db[i] == 2 and in_db[i] >= 2:
            eight_graph += 1
            
        elif out_db[i] == 0 and in_db[i] >= 1:
            list_graph += 1
            
    donut_graph = out_db[node] - (eight_graph + list_graph)
    
    answer.append(node)                       
    answer.append(donut_graph)
    answer.append(list_graph)
    answer.append(eight_graph)
    
    return answer