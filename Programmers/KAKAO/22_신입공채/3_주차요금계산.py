import math

def convert(time):
    hh, mm = time.split(':')
    return int(hh) * 60 + int(mm)  # 분으로 리턴

def solution(fees, records):
    inDic = {}
    resultDic = {}

    for rec in records:
        time, num, inout, = rec.split()
        if inout == 'IN':
            inDic[num] = convert(time)
            if num not in resultDic:
                resultDic[num] = 0
        else:  # OUT
            resultDic[num] += convert(time) - inDic[num]
            del inDic[num]

    for k, v in inDic.items():  # 출차 내역 없는 차량들 처리
        resultDic[k] += (23 * 60 + 59) - v

    answer = []

    for k, v in sorted(resultDic.items()):
        if v <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((v - fees[0]) / fees[2]) * fees[3])

    return answer