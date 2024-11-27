n = int(input())

cows=[]
for _ in range(n):
    arrival, check_time = map(int, input().split())
    cows.append((arrival, check_time))

s_cows = sorted(cows, key=lambda x: x[0])

total = s_cows[0][0]+s_cows[0][1]

for i in range(1, len(s_cows)):
    arrival, check_time = s_cows[i]
    if total < arrival:
        total = arrival + check_time
    else:
        total += check_time

print(total)