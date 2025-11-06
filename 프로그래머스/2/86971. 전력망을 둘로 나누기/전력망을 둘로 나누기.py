from collections import deque
def solution(n, wires):
    
    adj = [[] for _ in range(n+1)]
    for a, b in wires:
        adj[a].append(b)
        adj[b].append(a)
    
    def bfs(start_node, block_a, block_b):
        visited = [False] * (n+1)
        
        q = deque()
        q.append(start_node)
        visited[start_node] = True
        count = 1
        while q:
            cur = q.popleft()
            for nxt_node in adj[cur]:
                if (cur == block_a and nxt_node == block_b) or (cur == block_b and nxt_node == block_a):
                    continue
                if not visited[nxt_node]:
                    visited[nxt_node] = True
                    q.append(nxt_node)
                    count += 1
        return count
    
    answer = n
    for a, b in wires:
        cnt = bfs(a, a, b)
        diff = abs(n - 2*cnt)
        if diff < answer:
            answer = diff
            
    return answer