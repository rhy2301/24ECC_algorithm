v = int(input())
e = int(input())

adj = [[0 for _ in range(v)] for _ in range(v)]
for _ in range(e):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a][b], adj[b][a] = 1, 1

def DFS(s, visited):
    global ans 
    ans += 1
    visited[s] = True
    
    for v in range(v):
        if adj[s][v] != 0:
            if visited[v] == False:
                DFS(v, visited)
ans = -1
DFS(0, [False]*v)
print(ans)