import sys
input = sys.stdin.read

def merge_sort(A, p, r, K, save_counter):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, K, save_counter)         
        merge_sort(A, q + 1, r, K, save_counter)     
        merge(A, p, q, r, K, save_counter)           

def merge(A, p, q, r, K, save_counter):
    i, j, t = p, q + 1, 0
    tmp = []
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1        
  
        save_counter[0] += 1
        if save_counter[0] == K:
            print(tmp[-1])
            sys.exit()  
    
    while i <= q:
        tmp.append(A[i])
        i += 1
        save_counter[0] += 1
        if save_counter[0] == K:
            print(tmp[-1])
            sys.exit()  
    
    while j <= r:
        tmp.append(A[j])
        j += 1
        save_counter[0] += 1
        if save_counter[0] == K:
            print(tmp[-1])
            sys.exit()      
    
    for i in range(len(tmp)):
        A[p + i] = tmp[i]

data = input().split()
N, K = int(data[0]), int(data[1])
A = list(map(int, data[2:]))
save_counter = [0]  
merge_sort(A, 0, N - 1, K, save_counter)
print(-1)
