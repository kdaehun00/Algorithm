import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    nodes = [(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: (-x[1], x[0]))
    
    def insert(parent, child):
        cx, cy, cid = child
        
        if parent[0] > cx:
            if parent[3] is None:
                parent[3] = [cx, cy, cid, None, None]
            else:
                insert(parent[3], child)
            
        else:
            if parent[4] is None:
                parent[4] = [cx, cy, cid, None, None]
            else:
                insert(parent[4], child)
    
    root_node = [*nodes[0], None, None]
    for node in nodes[1:]:
        insert(root_node, node)
        
    def preorder(node):
        if node is None:
            return []
        else:
            return [node[2]] + preorder(node[3]) + preorder(node[4])
        
    def postorder(node):
        if node is None:
            return []
        return postorder(node[3]) + postorder(node[4]) + [node[2]]
    
    return [preorder(root_node), postorder(root_node)]