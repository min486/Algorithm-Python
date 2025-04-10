def solution(participant, completion):
    dct = {}
    for i in participant:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
            
    for j in completion:
        if j in dct:
            dct[j] -= 1
            
    for k, v in dct.items():
        if v > 0:
            return k