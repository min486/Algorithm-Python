def solution(s):
    mid = len(s) // 2
    
    if len(s) % 2 == 1:
        return s[mid]
    else:
        return s[mid-1 : mid+1]