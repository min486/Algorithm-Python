from itertools import combinations

def solution(numbers):
    sset = set()
    for i in combinations(numbers, 2):
        sset.add(sum(i))
        
    li = list(sset)
    li.sort()
    
    return li