dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(x,y):
    if field[x][y] == -1:
        return
    queue = [(x,y)]
    while queue:
        a, b = queue.pop(0)
        for i in range(4):
            na, nb = a+dx[i], b+dy[i]
            if na < 0 or na >= n or nb < 0 or nb >= m:
                continue
            if field[na][nb] == 1:
                queue.append((na, nb))
                field[na][nb] = -1 