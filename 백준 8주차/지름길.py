import heapq

N, D = map(int, input().split())  
shortcuts = [tuple(map(int, input().split())) for _ in range(N)]

INF = float('inf')
distance = [INF] * (D + 1)
distance[0] = 0

for i in range(D):
    distance[i + 1] = min(distance[i + 1], distance[i] + 1)
    
    for start, end, length in shortcuts:
        if start == i and end <= D and distance[end] > distance[start] + length:
            distance[end] = distance[start] + length


print(distance[D])
