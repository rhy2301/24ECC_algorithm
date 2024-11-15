import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.read
data = input().split()


n, m = map(int, data[:2])
A = list(map(int, data[2:n+2]))
queries = data[n+2:]


A.sort()


result = []
for i in range(m):
    query = queries[i*2:(i+1)*2]
    q_type = int(query[0])
    if q_type == 1:
        k = int(query[1])
        
        result.append(n - bisect_left(A, k))
    elif q_type == 2:
        k = int(query[1])
        
        result.append(n - bisect_right(A, k))
    elif q_type == 3:
        i = int(query[1])
        j = int(query[2])
        
        result.append(bisect_right(A, j) - bisect_left(A, i))


sys.stdout.write("\n".join(map(str, result)) + "\n")
