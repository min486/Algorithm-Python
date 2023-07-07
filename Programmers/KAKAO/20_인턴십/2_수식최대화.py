import re
from itertools import permutations 

def solution(expression):
    operators = list(permutations(['-', '+', '*'], 3))
    expre = re.split('([-+*])', expression)

    answer_li = []
    for opes in operators:
        exp = expre[:]
        for ope in opes:  # 연산자 3개에서 1개씩
            while ope in exp:
                idx = exp.index(ope)
                exp[idx-1] = str(eval(exp[idx-1] + ope + exp[idx+1]))
                del exp[idx:idx+2]
        answer_li.append(abs(int(exp[0])))
    return max(answer_li)