def stack_sequence(n, sequence):
    stack = []
    operations =[]
    current = 1

    for number in sequence:
        while current <= number:
            stack.append(current)
            operations.append('+')
            current += 1

        if stack[-1] == number:
            stack.pop()
            operations.append('-')
        else:
            return ["NO"]
        
    return operations

n = int(input("n을 입력하세요: "))
sequence = [int(input()) for _ in range(n)]

result = stack_sequence(n, sequence)
for op in result:
    print(op)
