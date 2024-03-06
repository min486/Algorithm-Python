# 매우비동의 / 비동의 / 약간비동의 / 모름 / 약간동의 / 동의 / 매우동의
# 1 / 2 / 3 / 4 / 5 / 6 / 7  -> choices
# 3 / 2 / 1 / x / 1 / 2 / 3  -> 점수 획득
# (앞 검사자)       (뒤 검사자)

from collections import defaultdict

def solution(survey, choices):
    chr2score = defaultdict(int)

    for (a, b), choice in zip(survey, choices):
        if choice < 4:
            chr2score[a] += 4 - choice
        elif choice > 4:
            chr2score[b] += choice - 4

    type1, type2 = ['R', 'C', 'J', 'A'], ['T', 'F', 'M', 'N']
    answer = ''

    for t1, t2 in zip(type1, type2):
        if chr2score[t1] > chr2score[t2] or (chr2score[t1] == chr2score[t2] and t1 < t2):
            answer += t1
        else:
            answer += t2

    return answer