def solution(arr):
    li = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            continue
        else:
            li.append(arr[i])
            
    return li