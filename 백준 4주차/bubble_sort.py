def bubble_sort(arr, N, K):
    swap_count = 0

    for last in range(N-1, 0 ,-1):
        for i in range(last):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_count += 1

                if swap_count == K:
                    print(" ".join(map(str,arr)))
                    return
    print(-1)
    
        

N, K = map(int,input().split())
A = list(map(int,input().split()))
bubble_sort(A, N, K)

