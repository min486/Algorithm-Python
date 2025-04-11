def solution(n):
    # 0, 1은 소수 아님
    li = [False, False] + [True]*(n-1)
    
    for i in range(2, int(n**0.5)+1):
        if li[i]:  # i가 소수이면
            for j in range(i*i, n+1, i):  # i의 배수들은 소수 아님
                li[j] = False
                
    return sum(li)