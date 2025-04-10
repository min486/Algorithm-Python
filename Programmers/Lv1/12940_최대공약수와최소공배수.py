import math

def solution(n, m):
    max_div = math.gcd(n, m)
    min_mul = n*m // math.gcd(n, m)
    
    return [max_div, min_mul]