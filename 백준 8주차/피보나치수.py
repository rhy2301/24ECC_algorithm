def fib(n):
    global code1_count
    if n == 1 or n == 2:
        code1_count += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fibonacci(n):
    global code2_count
    f = [0] * (n + 1)
    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        code2_count += 1
    return f[n]

n = int(input())

code1_count = 0
code2_count = 0

fib(n)
fibonacci(n)

print(code1_count, code2_count)