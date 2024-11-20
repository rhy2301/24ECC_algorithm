from collections import defaultdict

n = int(input())
players = [input() for _ in range(n)]

first_letter_count = defaultdict(int)
for player in players:
    first_letter_count[player[0]] += 1

result = [letter for letter, count in first_letter_count.items() if count >= 5]

if result:
    print("".join(sorted(result)))
else:
    print("PREDAJA")
