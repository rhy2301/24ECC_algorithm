N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
queries = list(map(int, input().split()))

def binary_search(A, key, low, high):
    while low <= high:
        middle = (low+high)//2
        if key == A[middle]:
            return 1
        elif(key<A[middle]):
            high = middle - 1
        else:
            low = middle + 1
    return 0
    

results = [binary_search(A, query, 0, N-1) for query in queries]
print("\n".join(map(str, results)))