def solution(x):
    total = 0
    for i in str(x):
        total += int(i)
        
    if x % total == 0:
        return True
    else: 
        return False