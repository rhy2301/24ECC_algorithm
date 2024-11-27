N = int(input())

level = []
for _ in range(N):
    point = int(input())
    level.append(point)

count = 0

for i in range(N-2, -1, -1):
    while level[i]>=level[i+1]:
        level[i] -= 1
        count += 1

print(count)