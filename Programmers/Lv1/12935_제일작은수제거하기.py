def solution(arr):
    mn = min(arr)
    arr.remove(mn)
    
    if len(arr) == 0:
        return [-1]
    
    return arr