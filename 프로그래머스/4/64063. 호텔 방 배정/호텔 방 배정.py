def solution(k, room_number):
    parent = {}

    def find(x):
        path = []
        while x in parent:
            path.append(x)
            x = parent[x]
        for node in path:
            parent[node] = x + 1
        parent[x] = x + 1
        return x

    answer = []
    for room in room_number:
        available = find(room)
        answer.append(available)
    return answer