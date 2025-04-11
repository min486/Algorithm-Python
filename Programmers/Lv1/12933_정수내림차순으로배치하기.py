def solution(n):
    li = list(str(n))
    li.sort(reverse=True)
    ans = ''.join(li)
    
    return int(ans)