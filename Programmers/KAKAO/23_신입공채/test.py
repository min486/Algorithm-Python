# from itertools import permutations
from itertools import product

# for item in permutations(['1', '2', '3'], 2):
for item in product([1, 2, 3], repeat=2):

    print(item)