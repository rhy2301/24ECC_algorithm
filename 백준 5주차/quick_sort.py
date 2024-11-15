import sys
input = sys.stdin.read

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def partition(A, p, r):
    global count, result
    x = A[r]  
    i = p - 1  
    for j in range(p, r):  
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]  
            count += 1
            if count == K:
                result = (min(A[i], A[j]), max(A[i], A[j]))  
    if i + 1 != r:  
        A[i + 1], A[r] = A[r], A[i + 1]
        count += 1
        if count == K:
            result = (min(A[i + 1], A[r]), max(A[i + 1], A[r]))  
    return i + 1


data = input().split()
N, K = int(data[0]), int(data[1])
A = list(map(int, data[2:]))

count = 0 
result = -1  

quick_sort(A, 0, N - 1)


if result == -1:
    print(-1)
else:
    print(result[0], result[1])
