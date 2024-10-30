K = int(input("입력할 정수의 개수를 입력하세요: "))

stack = []

for _ in range(K):
    number = int(input())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))