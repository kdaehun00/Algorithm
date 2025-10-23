def solution(user_id, banned_id):
    banned_db = []
    for b_id in banned_id:
        temp = []
        for u_id in user_id:
            if len(u_id) != len(b_id):
                continue
            if all(bc == "*" or bc == uc for bc, uc in zip(b_id, u_id)):
                temp.append(u_id)
        banned_db.append(temp)
    
    result = set()
    
    def dfs(depth, current):
        if depth == len(banned_db):
            result.add(frozenset(current))
            return
        for user in banned_db[depth]:
            if user not in current:
                dfs(depth + 1, current + [user])
    
    dfs(0, [])
    return len(result)