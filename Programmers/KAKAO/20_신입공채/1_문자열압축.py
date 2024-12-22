import re

def solution(s):
    if len(s) <= 2:
        return len(s)

    resultCnt = []
    for i in range(1, len(s)//2 + 1):
        reList = re.sub('(\w{%i})' %i, '\g<1> ', s).split()
        cnt = 1
        result = []
        for j in range(len(reList)):
            if j < len(reList)-1 and reList[j] == reList[j+1]:
                cnt += 1
            else:
                if cnt == 1:
                    result.append(reList[j])
                else:
                    result.append(str(cnt) + reList[j])
                    cnt = 1
        resultCnt.append(len(''.join(result)))
    return min(resultCnt)