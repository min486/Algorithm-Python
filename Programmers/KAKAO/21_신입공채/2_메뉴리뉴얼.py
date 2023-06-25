from itertools import combinations

def solution(orders, course):
    answer = []
    menuDics = [{} for _ in range(11)]
    maxCnt = [0 for _ in range(11)]

    for st in orders:
        for num in range(2, len(st) + 1):
            for i in combinations(sorted(st), num):
                k = ''.join(i)
                if k in menuDics[num]:
                    menuDics[num][k] += 1
                    maxCnt[num] = max(maxCnt[num], menuDics[num][k])
                else:
                    menuDics[num][k] = 1

    for num in course:
        for k, v in menuDics[num].items():
            if v >= 2 and v == maxCnt[num]:
                answer.append(k)

    return sorted(answer)