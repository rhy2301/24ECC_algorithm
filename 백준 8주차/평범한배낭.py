def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W+1)] for x in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, W+1):
             if wt[i-1] > w:
                 A[i][w] = A[i-1][w]
             else:
                 valWith = val[i-1] + A[i-1][w-wt[i-1]]
                 valWithout = A[i-1][w]
                 A[i][w] = max(valWith, valWithout)
                 
    return A[n][W]

n, k = map(int, input().split())
wt, val = zip(*[tuple(map(int, input().split())) for _ in range(n)])

wt = list(wt)
val = list(val)

print(knapSack_dp(k, wt, val, n))