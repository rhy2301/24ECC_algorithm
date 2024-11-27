from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for comb in combinations(cards, 3):
    current_sum = sum(comb)
    if current_sum <= M:
        max_sum = max(max_sum, current_sum)

print(max_sum)