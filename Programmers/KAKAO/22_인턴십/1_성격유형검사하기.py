# 매우비동 / 비동 / 약간비동 / 모름 / 약간동 / 동 / 매우동
# 1       / 2    / 3       / 4    / 5     / 6  / 7  -> choices
# 3       / 2    / 1       / x    / 1     / 2  / 3  -> 점수 획득
# (앞 검사자)                       (뒤 검사자)

from collections import defaultdict

def solution(survey, choices):
    ddic = defaultdict(int)
    for i in range(len(choices)):
        if choices[i] <= 3:
            ddic[survey[i][0]] += 4 - choices[i]  # 비동의쪽 점수 획득
        else: 
            ddic[survey[i][1]] += choices[i] - 4  # 동의쪽 점수 획득
    
    answer = ''
    if ddic['R'] >= ddic['T']: 
        answer += 'R'
    else: 
        answer += 'T'

    if ddic['C'] >= ddic['F']: 
        answer += 'C'
    else: 
        answer += 'F'
    
    if ddic['J'] >= ddic['M']: 
        answer += 'J'
    else: 
        answer += 'M'
    
    if ddic['A'] >= ddic['N']: 
        answer += 'A'
    else: 
        answer += 'N'   
    
    return answer