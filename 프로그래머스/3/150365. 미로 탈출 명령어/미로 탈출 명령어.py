def solution(n, m, x, y, r, c, k):
    x, y, r, c = x-1, y-1, r-1, c-1
    directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

    path = ''
    cur_x, cur_y = x, y

    for step in range(k):
        for d, dx, dy in directions:
            nx, ny = cur_x + dx, cur_y + dy
            if 0 <= nx < n and 0 <= ny < m:
                remain = k - step - 1
                dist = abs(r - nx) + abs(c - ny)
                if dist <= remain and (remain - dist) % 2 == 0:
                    path += d
                    cur_x, cur_y = nx, ny
                    break
        else:
            return "impossible"

    return path if (cur_x, cur_y) == (r, c) else "impossible"