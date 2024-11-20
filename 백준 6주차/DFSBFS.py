from collections import defaultdict, deque

def dfs(graph, start, visited, result):
    visited[start] = True
    result.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)

def bfs(graph, start):
    visited = [False] * (len(graph))
    queue = deque([start])
    visited[start] = True
    result = []
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result


n, m, v = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for key in graph:
    graph[key].sort()


dfs_result = []
visited = [False] * (n + 1)
dfs(graph, v, visited, dfs_result)

bfs_result = bfs(graph, v)


print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
