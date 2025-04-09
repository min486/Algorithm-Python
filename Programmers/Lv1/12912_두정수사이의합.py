def solution(a, b):
    ans = 0
    if a <= b:
        for i in range(a, b+1):
            ans += i
    else:
        for j in range(b, a+1):
            ans += j
            
    return ans