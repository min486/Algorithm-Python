from itertools import permutations

n, k = int(input()), int(input())
cards = [input() for _ in range(n)]
se = set()

for per in permutations(cards, k):
    se.add(''.join(per))

print(len(se))