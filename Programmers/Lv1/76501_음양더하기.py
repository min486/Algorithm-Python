def solution(absolutes, signs):
    for idx, i in enumerate(signs):
        if i == False:
            absolutes[idx] = -absolutes[idx]
    
    return sum(absolutes)