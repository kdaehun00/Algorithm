def solution(commands):
    answer = []
    parent = {(r, c): (r, c) for r in range(1, 51) for c in range(1, 51)}
    value = {(r, c): "" for r in range(1, 51) for c in range(1, 51)}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return
        parent[b] = a

    for cmd in commands:
        cmd = cmd.split()
        act = cmd[0]

        if act == "UPDATE":
            if len(cmd) == 4:
                r, c, v = int(cmd[1]), int(cmd[2]), cmd[3]
                value[find((r, c))] = v
            else:
                v1, v2 = cmd[1], cmd[2]
                for k in value:
                    if value[k] == v1:
                        value[k] = v2

        elif act == "MERGE":
            r1, c1, r2, c2 = map(int, cmd[1:])
            p1, p2 = find((r1, c1)), find((r2, c2))
            if p1 == p2:
                continue
            val = value[p1] if value[p1] != "" else value[p2]
            union(p1, p2)
            value[find(p1)] = val

        elif act == "UNMERGE":
            r, c = int(cmd[1]), int(cmd[2])
            p = find((r, c))
            keep = value[p]
            same_group = [k for k in parent if find(k) == p]
            for k in same_group:
                parent[k] = k
                value[k] = ""
            value[(r, c)] = keep

        elif act == "PRINT":
            r, c = int(cmd[1]), int(cmd[2])
            v = value[find((r, c))]
            answer.append(v if v else "EMPTY")

    return answer