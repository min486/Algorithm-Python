def solution(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i]*b[i]
    
    return total